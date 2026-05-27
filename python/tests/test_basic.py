"""Basic smoke tests against the bundled specs.json."""

from passport_photo_specs import (
    countries,
    documents,
    find_country,
    find_document,
    raw,
    __version__,
)


def test_version():
    assert __version__ == "1.3.0"


def test_countries_count():
    cs = countries()
    assert len(cs) >= 90, f"expected 90+ countries, got {len(cs)}"


def test_documents_count():
    docs = documents()
    assert len(docs) >= 200, f"expected 200+ documents, got {len(docs)}"


def test_find_known_country():
    italy = find_country("italy")
    assert italy is not None
    assert italy["name"].lower().startswith("ital")


def test_find_known_document():
    doc = find_document("italy-visa-photo")
    assert doc is not None
    assert doc["widthMm"] == 35
    assert doc["heightMm"] == 45


def test_country_lookup_by_doc_slug():
    italy = find_country("italy-visa-photo")
    assert italy is not None
    assert italy["id"] == "italy"


def test_find_unknown_returns_none():
    assert find_country("atlantis") is None
    assert find_document("atlantis-passport-photo") is None


def test_raw_is_dict_with_countries():
    data = raw()
    assert isinstance(data, dict)
    assert "countries" in data
