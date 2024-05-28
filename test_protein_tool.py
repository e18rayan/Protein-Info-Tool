import pytest
from Protein-Info import translate, prot_length, prot_MW, ex_coef

def test_translate():
  assert translate("ATGCACTAA") == "MH*"
  assert translate("TTATCTTGA") == "LS*"
  assert translate("ATGTAA") == "M*"
  with pytest.

def test_prot_length():


def test_prot_MW():


def test_ex_coef():


