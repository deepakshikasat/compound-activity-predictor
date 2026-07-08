from __future__ import annotations

def compute_compound_descriptors(smiles: str) -> dict:
    """Compute descriptor placeholders with RDKit when installed.

    Example aspirin SMILES: CC(=O)Oc1ccccc1C(=O)O
    """
    if not smiles or not isinstance(smiles, str):
        raise ValueError("SMILES must be a non-empty string")
    try:
        from rdkit import Chem
        from rdkit.Chem import Crippen, Descriptors, Lipinski, rdMolDescriptors
    except ImportError as exc:
        raise ImportError("Install rdkit to compute descriptors from SMILES") from exc
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    mw = Descriptors.MolWt(mol)
    logp = Crippen.MolLogP(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)
    return {
        "molecular_weight": mw,
        "logP": logp,
        "num_h_bond_donors": hbd,
        "num_h_bond_acceptors": hba,
        "num_rotatable_bonds": Lipinski.NumRotatableBonds(mol),
        "tpsa": rdMolDescriptors.CalcTPSA(mol),
        "num_aromatic_rings": rdMolDescriptors.CalcNumAromaticRings(mol),
        "fraction_sp3": rdMolDescriptors.CalcFractionCSP3(mol),
        "passes_lipinski": mw < 500 and logp < 5 and hbd <= 5 and hba <= 10,
    }
