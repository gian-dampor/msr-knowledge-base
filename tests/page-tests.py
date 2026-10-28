
import unittest
from pathlib import Path
from html.parser import HTMLParser


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.section_ids = []
        self.button_labels = []
        self.data_sources = []
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)

        if tag == "section" and "id" in attributes:
            self.section_ids.append(attributes["id"])

        if tag == "button":
            self.current_tag = "button"

        if tag == "td":
            self.current_tag = "td"

    def handle_data(self, data):
        text = data.strip()

        if not text:
            return

        if self.current_tag == "button":
            self.button_labels.append(text)

        if self.current_tag == "td":
            self.data_sources.append(text)

    def handle_endtag(self, tag):
        if tag == self.current_tag:
            self.current_tag = None


class TestMSRPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        page_path = Path(__file__).resolve().parents[1] / "index.html"
        cls.html = page_path.read_text(encoding="utf-8")

        cls.parser = PageParser()
        cls.parser.feed(cls.html)

    def test_page_has_title(self):
        self.assertIn("<title>MSR Knowledge Base</title>", self.html)

    def test_page_has_four_sections(self):
        expected = ["sources", "collection", "analysis", "venues"]

        for section_id in expected:
            self.assertIn(section_id, self.parser.section_ids)

    def test_page_has_four_navigation_buttons(self):
        expected = [
            "Data Sources",
            "Collection Methods",
            "Analysis Methods",
            "Publication Venues",
        ]

        for label in expected:
            self.assertIn(label, self.parser.button_labels)

    def test_data_sources_are_present(self):
        expected = [
            "GitHub",
            "Stack Overflow",
            "JIRA",
            "App Stores",
            "Travis CI / Jenkins",
            "Mailing Lists",
            "npm Registry",
        ]

        for source in expected:
            self.assertIn(source, self.parser.data_sources)

    def test_tab_switching_function_exists(self):
        self.assertIn("function showTab(tabId)", self.html)
        self.assertIn("classList.add('active')", self.html)


if __name__ == "__main__":
    unittest.main()
