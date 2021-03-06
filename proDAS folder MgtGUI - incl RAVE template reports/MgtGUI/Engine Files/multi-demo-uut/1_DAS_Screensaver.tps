O p t i o n   E x p l i c i t  
  
 ' *   < s c r i p t . t p s >  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' *     A U T H O R :   < J o a c h i m   A g o u >  
 ' *  
 ' *     D E S C R I P T I O N :  
 ' *     < V i s u a l   d e m o >  
 ' *  
 ' *     D A T E :   0 1 / 0 3 / 2 0 2 0    
 ' *  
 ' *     M O D I F I C A T I O N S :  
 ' *         D A T E                   W H O     V E R S I O N       D E S C R I P T I O N  
 ' *         - - - - - - - - - -       - - -     - - - - - - - -     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
 ' *         2 0 2 0 0 1 0 3           J O A     1 . 0               I n i t i a l   v e r s i o n  
 ' *         2 0 2 0 0 1 0 5           J O A     2 . 0               C l e a n u p   c o d e .   A d d e d   v e r b o s i t y .  
 ' *         2 0 2 0 0 1 0 5           J O A     3 . 0               I n c o r p o r a t e   R T D   D r i v e r   2   i n s t a n c e  
 ' *         2 0 2 0 0 2 1 1           J O A     4 . 0               A d d   n e w   D e m o   C o m p r e s s o r   R T D   p a g e s   w i t h   s p l i t   s c r e e n   g r a p h  
 ' *         2 0 2 0 0 2 1 1           J O A     5 . 0               A d d   n e w   F H D   a n d   w h i t e   t h e m e   d e m o   R T D   p a g e s  
 ' *         2 0 2 0 0 2 1 1           J O A     6 . 0               A d d   n e w   L i s t   R T D   p a g e   t e m p l a t e s  
 ' *         2 0 2 0 0 2 1 2           J O A     7 . 0               A d d   n e w   P B S   s t a t u s   p a g e   t e m p l a t e  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * *   L O C A L   V A R I A B L E   D E C L A R A T I O N S   * * * * * * * * * * * * * * * * * * * * * * * *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 d i m   B o o 1 ,   C y c l e ,   B i g _ C y c l e  
 c h a n n e l   " M a t h _ F l o a t 1 ,   M a t h _ F l o a t 2 ,   M a t h _ F l o a t 3 ,   M a t h _ F l o a t 4 ,   M a t h _ F l o a t 5 ,   M a t h _ B o o l 1 ,   M a t h _ B o o l 2 ,   S i m _ C o m p r e s s o r _ P R ,   S i m _ C o m p r e s s o r _ W ,   S i m _ C o m p r e s s o r _ R e s p o n s e _ S e l e c t o r ,   S i m _ C o m p r e s s o r _ S e l e c t o r ,   D e m o _ J e t E n g i n e _ F l i g h t _ S e l e c t o r "  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   P R E R E Q U I S I T E S   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " * * *   S C R E E N S A V E R   * * * "  
 n o t e "   "  
  
 ' s h o w _ v i e w   " m a n g t p 5 - r t d 1 " ,   " V i e w   0 " ,   " x x x x x . v "  
 ' s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " x x x x x . v "  
 ' s h o w _ v i e w   " r t d 1 h o s t " ,   " V i e w   0 " ,   " x x x x x . v "  
 ' r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d " ,   R E P O R T   &   " D e m o " ,   B L A C K  
 ' d e l a y   5  
  
 i n s t r u c t i o n   " B e f o r e   y o u   s t a r t : " , S K I P  
 	 I f   s k i p G V   =   T r u e   T h e n  
 	 r e s u l t   " I n s t r u c t i o n s   s k i p p e d ! " ,   R E P O R T ,   R E D  
 	 E n d   I f  
  
 n o t e   " >   V e r i f y   t h e   R T D   p a g e s   ( . v   f i l e s )   o f   t h e   t e s t   p r o c e d u r e   a r e   d e f i n e d   i n   t h e   R T E . "  
 n o t e   " >   V e r i f y   t h e   R T D 1   c o m p u t e r   h a s   s t a r t e d   R T D   D r i v e r   w i t h   V i e w   0   a n d   V i e w   1 . "  
 n o t e   "   "  
 n o t e   "   "  
 n o t e   "   "  
  
 p r o m p t _ b o o   " D i d   y o u   u n d e r s t a n d   t h e   i n s t r u c t i o n s ? " , b o o 1  
 	 I f   B o o 1   =   f a l s e   T h e n  
 	 r e s u l t   " D e m o n s t r a t i o n   C a n c e l e d ! " ,   R E P O R T   ,   R E D  
 	 q u i t  
 	 E n d   I f  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   D E M O   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " S t a r t i n g   s c r e e n s a v e r   . . . "  
  
 C y c l e   =   1  
 W h i l e   C y c l e < = 5  
  
  
 n o t e   " T e m p l a t e s   . . . "  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 0 _ T e m p l a t e _ 1 9 2 0 _ 1 2 0 0 . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 0 _ T e m p l a t e _ 1 9 2 0 _ 1 2 0 0 _ P a n e l . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " D A S   . . . "  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 1 _ C l o c k . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   2  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 1 _ D A S _ C o n t r o l . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   4  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 1 _ P B S _ P u r g e _ C o n t r o l . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   3  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 1 _ P B S _ S t a t u s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   2  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " D e m o n s t r a t i o n   . . . "  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ A l a r m s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1  
  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ C a l c u l a t i o n s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   2  
  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   1  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   2  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   0  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   0  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   1  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   1 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   1 0 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   1 0 0 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   1 0 0 0 0  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 8 6  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   2 1  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   0  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 1 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 2 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 3 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 4 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 2 0 1  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 1 9 9  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 1 9 6  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 1 9 5  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   - 2 5 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   - 1 9 4  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   1 . 1 2 3  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   8  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   8 8  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   1 0 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   1 1 1  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
  
 d e l a y   1  
  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ C o n v e r s i o n _ D e c H e x B i n . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   2  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ L a n g u a g e s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ P o l a r . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ P r o f i l e _ P l o t . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   2  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   1 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   2 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   3 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   4 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   5 0  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
 d e l a y   4  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   1 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   1 2 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   1 3 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   1 4 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   1 5 0  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
 d e l a y   5  
  
 s e t _ c h a n n e l   M a t h _ F l o a t 1 ,   1 . 1 2 3  
 s e t _ c h a n n e l   M a t h _ F l o a t 2 ,   8  
 s e t _ c h a n n e l   M a t h _ F l o a t 3 ,   8 8  
 s e t _ c h a n n e l   M a t h _ F l o a t 4 ,   1 0 0  
 s e t _ c h a n n e l   M a t h _ F l o a t 5 ,   1 1 1  
 s e t _ c h a n n e l   M a t h _ B o o l 1 ,   1  
 s e t _ c h a n n e l   M a t h _ B o o l 2 ,   1  
 d e l a y   5  
  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ S i m u l a t i o n s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ S i m u l a t i o n s _ 3 2 C h a n n e l s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   2  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ S i m u l a t i o n s 2 . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1 0  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ L i s t . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ L i s t _ C o m p a c t . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " C o m p r e s s o r   . . . "  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 3 _ C o m p r e s s o r M a p . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 3 _ C o m p r e s s o r M a p _ P a n e l . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1 0  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ S e l e c t o r ,   0  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ R e s p o n s e _ S e l e c t o r ,   2  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   0  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   0  
 d e l a y   5  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   0 . 9  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   4  
 d e l a y   3  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   1  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   5  
 d e l a y   3  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   1 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   6  
 d e l a y   3  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   2 . 3  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 0  
 d e l a y   2  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   6 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 8  
 d e l a y   3  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   6  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 8  
 d e l a y   3  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ R e s p o n s e _ S e l e c t o r ,   1  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   7  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   2 0  
 d e l a y   5  
  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 3 _ C o m p r e s s o r M a p _ P a n e l _ M u l t i . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 3 _ C o m p r e s s o r M a p _ P a n e l _ M u l t i _ D a r k . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1 0  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ S e l e c t o r ,   0  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ R e s p o n s e _ S e l e c t o r ,   2  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   0  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   0  
 d e l a y   1  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   1 . 3  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   6  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 5 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   1 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   5 . 8  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 5 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   1 . 6  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 5 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   1 . 6  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   7 . 7  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 6 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   2  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   7  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 6 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   2 . 2  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   6 . 4  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 6 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   2 . 3  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 0 . 6  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 7 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   2 . 7  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   9 . 5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 7 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   3  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   8 . 2  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 7 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   2 . 8  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 2 . 8  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 7 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   4  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 2  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 7 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   4 . 2  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 0 . 5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 7 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   3 . 2  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 4 . 3  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 8 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   4 . 3  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 3 . 5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 8 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   4 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 1 . 5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 8 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   3 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 6  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 8 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   4 . 6  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 8 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   5 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 3 . 5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 8 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   4  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 7 . 5  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 9 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 7  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 9 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   6 . 3  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 6 . 4  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 9 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   4 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 8 . 8  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 9 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   5 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 8 . 6  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 9 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   7 . 3  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 8 . 3  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 9 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   2 0 . 2  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 1 0 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   6  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   2 0  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 1 0 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   7 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   1 9 . 9  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 1 0 0 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   5 . 4  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   2 1  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 1 0 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   6 . 5  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   2 0 . 9  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 1 0 5 "  
  
  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ P R ,   8  
 s e t _ c h a n n e l   S i m _ C o m p r e s s o r _ W ,   2 0 . 6  
 d e l a y   1  
 d o _ f u l l s e t   1 ,   " S t e a d y - s t a t e   m e a s u r e m e n t   c o m p l e t e d " ,   " S p e e d _ 1 0 5 "  
  
 b e e p   1  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " J e t   E n g i n e   . . . "  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 4 _ J e t E n g i n e _ M a i n P a g e . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 4 _ J e t E n g i n e _ P i c t u r e . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1 0  
  
 s e t _ c h a n n e l   D e m o _ J e t E n g i n e _ F l i g h t _ S e l e c t o r ,   1  
 d e l a y   2  
  
 s e t _ c h a n n e l   D e m o _ J e t E n g i n e _ F l i g h t _ S e l e c t o r ,   3  
 d e l a y   5  
  
 s e t _ c h a n n e l   D e m o _ J e t E n g i n e _ F l i g h t _ S e l e c t o r ,   6  
 d e l a y   5  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 4 _ J e t E n g i n e _ V i b S u r v e y . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
  
 d e l a y   1  
  
 s e t _ c h a n n e l   D e m o _ J e t E n g i n e _ F l i g h t _ S e l e c t o r ,   1  
 d e l a y   3  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " B e l l m o u t h   M a s s   F l o w   . . . "  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 5 _ B e l l m o u t h _ M a s s _ F l o w . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   2  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " I n d u s t r i a l   G a s   T u r b i n e   . . . "  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 6 _ G a s T u r b i n e _ M e c h a n i c a l _ V e r i f . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 6 _ G a s T u r b i n e _ P i c t u r e . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 6 _ G a s T u r b i n e _ S p e e d _ T a r g e t s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 6 _ G a s T u r b i n e _ S p e e d _ T o r q u e . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 6 _ G a s T u r b i n e _ T h e r m o _ V e r i f . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " E m i s s i o n s   . . . "  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 7 _ E m i s s i o n s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " F u l l   H D   f o r m a t   . . . "  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " F H D _ 0 _ T e m p l a t e _ 1 9 2 0 _ 1 0 8 0 . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " F H D _ 0 _ T e m p l a t e _ 1 9 2 0 _ 1 0 8 0 _ P a n e l . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " F H D _ 2 _ C a l c u l a t i o n s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " F H D _ 2 _ S i m u l a t i o n s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " w h i t e   t h e m e   . . . "  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " W _ 0 _ T e m p l a t e _ 1 9 2 0 _ 1 2 0 0 . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " W _ 0 _ T e m p l a t e _ 1 9 2 0 _ 1 2 0 0 _ P a n e l . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   5  
  
 s h o w _ v i e w   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " W _ 2 _ C a l c u l a t i o n s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   1 " ,   R E P O R T ,   B L A C K  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   1  
  
 s h o w _ v i e w 2   " p r o d a s r t d 1 " ,   " V i e w   0 " ,   " 2 _ C a l c u l a t i o n s . v "  
 r e s u l t   " T h e   R e a l - T i m e   D i s p l a y   p a g e   h a s   b e e n   l o a d e d   o n   R T D   D r i v e r   2 " ,   R E P O R T ,   B L U E  
 r e s u l t   "   " ,   R E P O R T  
 d e l a y   7  
  
  
  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 n o t e   " N e x t   c y c l e   . . . "  
  
 r e s u l t   " C y c l e   C a l c u l a t i o n s   c o m p l e t e d " ,   R E P O R T   &   " C a l c u l a t i o n s   c y c l e " ,   B L U E  
  
 C y c l e   =   C y c l e   +   1  
  
 W e n d  
  
  
 r e s u l t   " A l l   c y c l e s   c o m p l e t e d ! " ,   R E P O R T ,   G R E E N  
  
 b e e p   5 