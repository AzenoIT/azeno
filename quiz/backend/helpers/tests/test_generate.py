import pytest

from helpers.gen_username.generate import generate_username


def test_username_generator_with_no_args(
    monkeypatch, nouns_temp_file, adjectives_temp_file
):
    monkeypatch.setattr(
        "helpers.gen_username.generate.adjectives", str(adjectives_temp_file)
    )
    monkeypatch.setattr("helpers.gen_username.generate.nouns", str(nouns_temp_file))
    users = generate_username()

    assert len(users) == 5
    assert len(set(users)) == len(users)


def test_username_generator_with_args(
    monkeypatch, nouns_temp_file, adjectives_temp_file
):
    monkeypatch.setattr(
        "helpers.gen_username.generate.adjectives", str(adjectives_temp_file)
    )
    monkeypatch.setattr("helpers.gen_username.generate.nouns", str(nouns_temp_file))
    users = generate_username(3)

    assert len(users) == 3
    assert len(set(users)) == len(users)
