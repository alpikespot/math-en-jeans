#include <vector>
#include <iostream>
#include "Piece.h"
using namespace std;

class Grille
{
public:
    Grille(int gr[6][6]);

    void afficher();
    void ajouter(Piece piece_aj);
    void mettre_dans_grille(Piece piece_aj);
    void retirer_dernier(int idx);

    int piece_manquante_dernier();

    bool verifier(Piece piece_test);
    bool verif_smileys(Piece piece_test);
    bool verif_complete();

public:
    int grille[6][6];
    int grille_originale[6][6];
    vector<Piece> pieces;


};