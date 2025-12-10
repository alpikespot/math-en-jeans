#pragma once


class Piece
{
public:
    Piece(int indx, int px=0, int py=0, int r=0, bool f = false);
public:
    int piece[3][3];
    char clr[4];
    int p_x, p_y, piece_idx;
    int rot;
    bool flip;

    void retourner();
    void flipper();
    void afficher();

    bool verifier(int grille[6][6]);
    

};
