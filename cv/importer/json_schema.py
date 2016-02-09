from jsonschema import validate

CV_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "CV",
    "description": "Someone's CV",
    "type": "object",
    "required": ["introduction", "name"],
    "properties": {
        "introduction": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "work_experience": {
            "type": "array",
            "items": {
                "title": "Work Experience",
                "required": ["from_date",
                             "to_date",
                             "role",
                             "company",
                             "location",
                             "description"],
                "type": "object",
                "properties": {
                    "from_date": {
                        "type": "string",
                        "description": "A date formatted as YYYY-MM-DD"
                    },
                    "to_date": {
                        "type": "string",
                        "description": "A date formatted as YYYY-MM-DD"
                    },
                    "role": {
                        "type": "string"
                    },
                    "company": {
                        "type": "string"
                    },
                    "location": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "highlights": {
                        "type": "string"
                    }
                }
            }
        },
        "volounteer_work": {
            "type": "array",
            "items": {
                "title": "Volounteer Work",
                "required": ["from_date",
                             "to_date",
                             "role",
                             "organization",
                             "description"],
                "type": "object",
                "properties": {
                    "from_date": {
                        "type": "string",
                        "description": "A date formatted as YYYY-MM-DD"
                    },
                    "to_date": {
                        "type": "string",
                        "description": "A date formatted as YYYY-MM-DD"
                    },
                    "role": {
                        "type": "string"
                    },
                    "organization": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            }
        },
        "courses": {
            "type": "array",
            "items": {
                "title": "Courses",
                "required": [
                             "description"],
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string"
                    }
                }
            }
        },
        "education": {
            "type": "array",
            "items": {
                "title": "Education",
                "required": ["from_date",
                             "to_date",
                             "degree",
                             "school",
                             "location",
                             "description"],
                "type": "object",
                "properties": {
                    "from_date": {
                        "type": "string",
                        "description": "A date formatted as YYYY-MM-DD"
                    },
                    "to_date": {
                        "type": "string",
                        "description": "A date formatted as YYYY-MM-DD"
                    },
                    "degree": {
                        "type": "string"
                    },
                    "school": {
                        "type": "string"
                    },
                    "location": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            }
        },
        "languages": {
            "type": "array",
            "items": {
                "title": "Languages Spoken",
                "required": ["language",
                             "level"],
                "type": "object",
                "properties": {
                    "language": {
                        "type": "string"
                    },
                    "level": {
                        "type": "string"
                    }
                }
            }
        }
    }
}

def validate_document(document):
    validate(document, CV_SCHEMA)
