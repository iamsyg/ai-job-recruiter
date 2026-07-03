# src/extract_jd_features.py

from dotenv import load_dotenv

load_dotenv()

from google import genai
import os
import json
from schema.jd_schema import JDSchema

from google.genai.errors import ServerError

def extract_jd_features(jd_text: str) -> JDSchema:

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    schema_json = JDSchema.model_json_schema()

    prompt = f"""
        You are an expert technical recruiter and talent intelligence analyst.

        Your task is to extract structured candidate-selection criteria from a job description.

        Return ONLY valid JSON that matches the provided schema.

        Schema:
        {json.dumps(schema_json, indent=2)}

        GENERAL RULES

        * Extract only information that affects candidate selection.
        * Do not invent information.
        * If a value is not explicitly stated or cannot be reasonably inferred, use null for scalar fields.
        * Use empty arrays for missing list fields.
        * Return valid JSON only.
        * Do not return markdown.
        * Do not return explanations.
        * Do not return comments.
        * Do not return code fences.
        * Follow the schema exactly.

        Normalization Rules

        * Remove duplicate or highly overlapping concepts.
        * Prefer the most general canonical category.
        * Do not return both a parent concept and its synonym.
        * Each list item should represent a unique signal.

        IGNORE THE FOLLOWING

        * Company introductions
        * Company history
        * Culture descriptions
        * Hiring philosophy
        * Team descriptions
        * Hackathon instructions
        * Explanatory text
        * Marketing language
        * Future responsibilities that do not imply candidate requirements

        FIELD DEFINITIONS

        preferred_locations

        * Primary locations explicitly preferred for hiring.
        * Include only locations that are stated as preferred.
        * Do not include locations that are merely acceptable.

        additional_locations

        * Locations that are acceptable but not explicitly preferred.
        * Include locations where candidates are welcomed or considered.
        * Do not duplicate locations from preferred_locations.

        relocation_preferred

        * True if the employer explicitly prefers or accepts candidates willing to relocate.
        * False otherwise.

        employment_type

        * Extract employment arrangements such as full-time, part-time, contract, internship, temporary, freelance, etc.

        work_mode

        * Extract work arrangements such as remote, hybrid, onsite, flexible, distributed, etc.

        experience_required

        * Extract the required experience range.
        * Populate minimum and maximum years whenever available.
        * If only one value is available, populate the corresponding field and leave the other null.

        must_have_skills

        * Extract only mandatory skills, technologies, concepts, methodologies, or technical competencies.
        * Return canonical taxonomy terms.
        * Normalize synonymous technologies into common concepts.
        * Prefer concepts over specific vendors or products whenever possible.
        * Keep entries concise and standardized.
        * Do not include explanations.

        preferred_skills

        * Extract skills that are beneficial but not required.
        * Return canonical taxonomy terms.
        * Keep entries concise and standardized.
        * Do not include explanations.

        role_focus

        * Extract the core problem domains relevant to the role.
        * Describe what kinds of systems, products, or technical areas the candidate is expected to work on.
        * Do not include responsibilities, management activities, mentoring, collaboration activities, or team structure.

        education_requirements

        * Extract explicit education requirements.
        * Include degrees, fields of study, certifications, or academic qualifications only if mentioned.

        company_type_preferences

        * Extract preferred employer backgrounds.
        * Examples include product companies, startups, enterprise software companies, marketplaces, SaaS companies, research organizations, consulting firms, etc.
        * Use generalized company categories rather than company names.

        negative_signals

        * Extract candidate attributes that reduce suitability.
        * Return normalized category names rather than full sentences.
        * Keep categories concise and machine-friendly.
        * Do not include explanations.
        * Merge similar exclusions into a single category when appropriate.

        notice_period

        * Extract the maximum preferred notice period in days.
        * Convert time references into an integer number of days when possible.

        salary_range

        * Extract the compensation range if provided.
        * Populate minimum and maximum values whenever available.
        * Use null for unavailable values.

        OUTPUT REQUIREMENTS

        * Output must be valid JSON.
        * Output must conform exactly to the schema.
        * Output must contain no additional fields.
        * Output must contain no explanatory text before or after the JSON.

        Job Description:

        {jd_text}

    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": JDSchema,
            }
        )

        return JDSchema.model_validate_json(response.text)
    
    except ServerError as e:
        raise RuntimeError(
            "The AI service is currently experiencing high demand. "
            "Please wait a few minutes and try again."
        ) from e

    except Exception as e:
        raise RuntimeError(
            f"Failed to extract job description features: {e}"
        ) from e