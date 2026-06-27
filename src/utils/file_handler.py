from __future__ import annotations

import os
from typing import Any

from pypdf import PdfReader
from docx import Document

class FileParser:
    """
    Handles robust parsing of different resume file formats.
    """
    
    @staticmethod
    def parse_file(file_path: str) -> str:
        """
        Parses PDF or DOCX files and returns the text content.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.pdf':
            return FileParser._parse_pdf(file_path)
        elif ext == '.docx':
            return FileParser._parse_docx(file_path)
        elif ext == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            raise ValueError(f"Unsupported file format: {ext}")

    @staticmethod
    def _parse_pdf(file_path: str) -> str:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    @staticmethod
    def _parse_docx(file_path: str) -> str:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
