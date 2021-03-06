O p t i o n   E x p l i c i t  
  
 ' *   < s c r i p t . t p s >  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' *     A U T H O R :   D o n   P e r e i r a  
 ' *  
 ' *     D E S C R I P T I O N :  
 ' *     P e r f o r m a n c e  
 ' *  
 ' *     D A T E :   9 / 1 5 / 2 0 0 5   8 : 3 9 : 4 0   A M  
 ' *  
 ' *     M O D I F I C A T I O N S :  
 ' *         D A T E                   W H O     N C R         D E S C R I P T I O N  
 ' *         - - - - - - - - - -       - - -     - - - - -     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
 ' *     V 1 . 0 1   0 6 / 0 2 / 2 0 0 3     R H     I n i t i a l  
 ' *     V 1 . 0 2   1 0 / 0 7 / 2 0 0 4     D P     A d d e d   s e t _ c h a n n e l   f o r   E N A B L E _ A L A R M S ' *  
 ' *     V 1 . 0 3   1 5 / 0 9 / 2 0 0 5     J C     C o n v e r t e d   t o   p h a s e   3   f o r m a t  
 ' *     V 1 . 0 4   0 4 / 1 2 / 2 0 0 9     D P     D e l e t e d   t e s t   b l o c k s   -   t h e y   w e r e   g e n e r a t i n g   e r r o r s  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 '   * * * * *   L O C A L   V A R I A B L E   D E C L A R A T I O N S   * * * * *  
 '   C h a n n e l   R e g i s t r a t i o n  
 c h a n n e l   " T q _ P T _ ,   S o l _ F u e l _ ,   n _ G G ,   n _ P T ,   t S t a b l e "  
  
  
 ' *     V 1 . 0 2   s h o w _ v i e w   f a c i l i t y ,   P e r f o r m a n c e . 0  
  
 ' *       *     *  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   4 2 . 5  
 s e t _ c h a n n e l   T q _ P T _ ,   6 2 2 0  
  
 i n s t r u c t i o n   " S t a b i l i z e   a t   I d l e   f o r   5   m i n u t e s "  
  
 w a i t   " n _ G G   <   8 6 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   a b o v e   8 6 0 0   r p m "  
 w a i t   " t S t a b l e   >   3 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   t S t a b l e   i s   l e s s   t h a n   3 0 0 s "  
 ' *     d e l a y   3 0 0  
 d e l a y   1 5  
  
 i n s t r u c t i o n     " A c c e l e r a t e   t o   n _ G G   =   1 0 5 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   1 0   m i n . "  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   5 0 . 8  
 s e t _ c h a n n e l   T q _ P T _ ,   6 3 9 0  
 w a i t   " n _ G G   >   1 0 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   a b o v e   8 6 0 0   r p m "  
 d e l a y   3 0  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   w a r m u p " ,   " W a r m U p "  
  
 '   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
  
 i n s t r u c t i o n     " A c c e l e r a t e   G G   s p e e d   t o   1 1 5 0 0   a n d   s e t   P T   t o   6 0 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   1 0   m i n . "  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   5 7 . 3  
 s e t _ c h a n n e l   T q _ P T _ ,   7 2 3 0  
 w a i t   " n _ G G   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 1 5 0 0   r p m "  
 w a i t   " n _ P T   >   6 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   3 0  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 1 _ P o i n t 1 " ,   " G G _ S p 1 _ P t 1 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   8 4 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   5 6 7 0  
 w a i t   " n _ G G   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 1 5 0 0   r p m "  
 w a i t   " n _ P T   >   8 4 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   8 4 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 1 _ P o i n t 2 " ,   " G G _ S p 1 _ P t 2 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 0 8 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   4 1 1 0  
 w a i t   " n _ G G   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 1 5 0 0   r p m "  
 w a i t   " n _ P T   >   1 0 8 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 0 8 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 1 _ P o i n t 3 " ,   " G G _ S p 1 _ P t 3 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 2 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   3 8 5 0  
 w a i t   " n _ G G   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 1 5 0 0   r p m "  
 w a i t   " n _ P T   >   1 1 2 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 2 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 1 _ P o i n t 4 " ,   " G G _ S p 1 _ P t 4 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 5 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   3 6 5 5  
 w a i t   " n _ G G   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 1 5 0 0   r p m "  
 w a i t   " n _ P T   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 5 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 1 _ P o i n t 5 " ,   " G G _ S p 1 _ P t 5 "  
  
 i n s t r u c t i o n     " D e c r e a s e   P T   s p e e d   t o   6 0 0 0 "  
 s e t _ c h a n n e l   T q _ P T _ ,   7 2 3 0  
 w a i t   " n _ P T   <   6 1 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   5  
  
 '   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
  
 i n s t r u c t i o n     " A c c e l e r a t e   G G   s p e e d   t o   1 2 0 0 0   a n d   s e t   P T   t o   7 2 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   1 0   m i n . "  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   6 2 . 2  
 s e t _ c h a n n e l   T q _ P T _ ,   7 5 8 0  
 w a i t   " n _ G G   >   1 2 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 0 0 0   r p m "  
 w a i t   " n _ P T   >   7 2 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   7 2 0 0   r p m "  
 d e l a y   3 0  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 2 _ P o i n t 1 " ,   " G G _ S p 2 _ P t 1 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   9 6 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   5 8 9 0  
 w a i t   " n _ G G   >   1 2 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 5 0 0   r p m "  
 w a i t   " n _ P T   >   9 6 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   9 6 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 2 _ P o i n t 2 " ,   " G G _ S p 2 _ P t 2 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 2 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   4 7 6 0  
 w a i t   " n _ G G   >   1 2 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 1 5 0 0   r p m "  
 w a i t   " n _ P T   >   1 1 2 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 2 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 2 _ P o i n t 3 " ,   " G G _ S p 2 _ P t 3 "  
  
 i n s t r u c t i o n     " D e c r e a s e   P T   s p e e d   t o   7 2 0 0 "  
 s e t _ c h a n n e l   T q _ P T _ ,   7 5 8 0  
 w a i t   " n _ P T   <   7 3 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   5  
  
 '   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
  
 i n s t r u c t i o n     " A c c e l e r a t e   G G   s p e e d   t o   1 2 5 0 0   a n d   s e t   P T   t o   6 0 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   1 0   m i n . "  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   7 0 . 6  
 s e t _ c h a n n e l   T q _ P T _ ,   1 0 9 6 0  
 w a i t   " n _ G G   >   1 2 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 5 0 0   r p m "  
 w a i t   " n _ P T   >   6 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   3 0  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 3 _ P o i n t 1 " ,   " G G _ S p 3 _ P t 1 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   8 4 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   8 9 9 0  
 w a i t   " n _ G G   >   1 2 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 5 0 0   r p m "  
 w a i t   " n _ P T   >   8 4 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   8 4 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 3 _ P o i n t 2 " ,   " G G _ S p 3 _ P t 2 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 0 8 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   7 0 2 0  
 w a i t   " n _ G G   >   1 2 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 5 0 0   r p m "  
 w a i t   " n _ P T   >   1 0 8 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 0 8 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 3 _ P o i n t 3 " ,   " G G _ S p 3 _ P t 3 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 2 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   6 6 9 0  
 w a i t   " n _ G G   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 5 0 0   r p m "  
 w a i t   " n _ P T   >   1 1 2 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 2 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 3 _ P o i n t 4 " ,   " G G _ S p 3 _ P t 4 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 5 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   6 4 4 0  
 w a i t   " n _ G G   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 5 0 0   r p m "  
 w a i t   " n _ P T   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 5 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 3 _ P o i n t 5 " ,   " G G _ S p 3 _ P t 5 "  
  
 i n s t r u c t i o n     " D e c r e a s e   P T   s p e e d   t o   6 0 0 0 "  
 s e t _ c h a n n e l   T q _ P T _ ,   1 1 0 0 0  
 w a i t   " n _ P T   <   6 1 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   5  
  
 '   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
  
 i n s t r u c t i o n     " A c c e l e r a t e   G G   s p e e d   t o   1 2 7 5 0   a n d   s e t   P T   t o   7 2 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   1 0   m i n . "  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   8 1 . 8  
 s e t _ c h a n n e l   T q _ P T _ ,   1 1 7 2 0  
 w a i t   " n _ G G   >   1 2 7 5 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 7 5 0   r p m "  
 w a i t   " n _ P T   >   7 2 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   7 2 0 0   r p m "  
 d e l a y   3 0  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 4 _ P o i n t 1 " ,   " G G _ S p 4 _ P t 1 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   9 6 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   9 6 6 0  
 w a i t   " n _ G G   >   1 2 7 5 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 7 5 0   r p m "  
 w a i t   " n _ P T   >   9 6 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   9 6 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 4 _ P o i n t 2 " ,   " G G _ S p 4 _ P t 2 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 2 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   8 2 9 0  
 w a i t   " n _ G G   >   1 2 7 5 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 2 7 5 0   r p m "  
 w a i t   " n _ P T   >   1 1 2 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 2 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 4 _ P o i n t 3 " ,   " G G _ S p 4 _ P t 3 "  
  
 i n s t r u c t i o n     " D e c r e a s e   P T   s p e e d   t o   7 2 0 0 "  
 s e t _ c h a n n e l   T q _ P T _ ,   1 1 7 2 0  
 w a i t   " n _ P T   <   7 3 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   5  
  
 '   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
  
 i n s t r u c t i o n     " A c c e l e r a t e   G G   s p e e d   t o   1 3 0 0 0   a n d   s e t   P T   t o   6 0 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   1 0   m i n . "  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   9 1 . 8  
 s e t _ c h a n n e l   T q _ P T _ ,   1 3 8 0 0  
 w a i t   " n _ G G   >   1 3 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 3 0 0 0   r p m "  
 w a i t   " n _ P T   >   6 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   3 0  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 5 _ P o i n t 1 " ,   " G G _ S p 5 _ P t 1 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   8 4 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   1 1 5 7 0  
 w a i t   " n _ G G   >   1 3 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 3 0 0 0   r p m "  
 w a i t   " n _ P T   >   8 4 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   8 4 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 5 _ P o i n t 2 " ,   " G G _ S p 5 _ P t 2 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 0 8 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   9 3 5 0  
 w a i t   " n _ G G   >   1 3 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 3 0 0 0   r p m "  
 w a i t   " n _ P T   >   1 0 8 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 0 8 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 5 _ P o i n t 3 " ,   " G G _ S p 5 _ P t 3 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 2 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   8 9 7 0  
 w a i t   " n _ G G   >   1 3 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 3 0 0 0   r p m "  
 w a i t   " n _ P T   >   1 1 2 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 2 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 5 _ P o i n t 4 " ,   " G G _ S p 5 _ P t 4 "  
  
 i n s t r u c t i o n     " I n c r e a s e   P T   s p e e d   t o   1 1 5 0 0 "  
 n o t e     " S t a b i l i z e   t h e   e n g i n e   f o r   2   m i n . "  
 s e t _ c h a n n e l   T q _ P T _ ,   8 7 0 0  
 w a i t   " n _ G G   >   1 3 0 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ G G   i s   b e l o w   1 3 0 0 0   r p m "  
 w a i t   " n _ P T   >   1 1 5 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   1 1 5 0 0   r p m "  
 d e l a y   5  
 d o _ f u l l s e t   5 ,   " P e r f   P o i n t :   S p e e d 5 _ P o i n t 5 " ,   " G G _ S p 5 _ P t 5 "  
  
 i n s t r u c t i o n     " D e c r e a s e   P T   s p e e d   t o   6 0 0 0 "  
 s e t _ c h a n n e l   T q _ P T _ ,   1 3 8 0 0  
 w a i t   " n _ P T   <   6 1 0 0 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   n _ P T   i s   b e l o w   6 0 0 0   r p m "  
 d e l a y   5  
  
 i n s t r u c t i o n   " C o n t i n u e   w i t h   G G   T e s t   M a x   p r o c e d u r e "  
 