O p t i o n   E x p l i c i t  
  
 ' *   < A u t o T h r o t t l e M K I I I . t p s >  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' *     A U T H O R :   < S h u w e n   G a o >  
 ' *  
 ' *     D E S C R I P T I O N :  
 ' *     < A u t o   T h r o t t l e   M K I I I   s t a n d a r d   T P >  
 ' *  
 ' *     D A T E :   6 / 1 9 / 2 0 1 5   4 : 0 4 : 1 3   P M  
 ' *  
 ' *     M O D I F I C A T I O N S :  
 ' *         D A T E                   W H O     N C R         D E S C R I P T I O N  
 ' *         - - - - - - - - - -       - - -     - - - - -     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
 ' *         6 / 1 9 / 2 0 1 5         S G                     A u t o T h r o t t l e M K I I I   s t a n d a r d   c o m m a n d s   t e s t i n g    
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 '   * * * * *   L O C A L   V A R I A B L E   D E C L A R A T I O N S   * * * * *  
 D i m   r e t u r n c o d e ,   r e t u r n v a l u e ,   s e t v a l u e ,   r e t V a l u e  
  
 '   C h a n n e l   R e g i s t r a t i o n  
 c h a n n e l   " P L A ,   F u e l O n ,   T L A ,   N 1 "  
  
 i n s t r u c t i o n   " P u t   t h r o t t l e   i n t o   a u t o   m o d e "  
  
 ' *   T e s t   A u t o T h r o t t l e   S t a r t   C o m m a n d  
 r e t u r n c o d e   =   a t _ s t a r t a u t o m o d e  
 r e s u l t   " r e t u r n c o d e   f o r   s t a r t a u t o m o d e   - > " &   r e t u r n c o d e   & " " ,   R E P O R T   &   " T h r o t t l e "  
  
 i f   r e t u r n c o d e   =   0   T h e n  
 ' *   T e s t   A u t o T h r o t t l e   M o v e   C o m m a n d 	  
 	 i n s t r u c t i o n   " M o v e   t h e   P L A   t o   0   d e g r e e "  
 	 r e t u r n c o d e   =   a t _ m o v e   ( " T L A " ,   0 ,   5 ,   7 . 0 ,   0 . 5 ,   1 . 0 )  
 ' 	 r e t u r n c o d e   =   a t _ m o v e   ( " N 1 " ,   0 ,   5 ,   7 ,   5 ,   1 )  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   M o v e   - >   " &   r e t u r n c o d e   & " .   M o v e   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   M o v e   - >   " &   r e t u r n c o d e   & " .   M o v e   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	 i n s t r u c t i o n   " M o v e   t h e   P L A   t o   1 0   d e g r e e "  
 	 r e t u r n c o d e   =   a t _ M o v e   ( " T L A " ,   1 0 ,   5 ,   7 . 0 ,   0 . 5 ,   1 . 0 )  
 ' 	 r e t u r n c o d e   =   a t _ M o v e   ( " N 1 " ,   6 5 0 ,   5 ,   7 . 0 ,   5 ,   1 . 0 )  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   M o v e   - >   " &   r e t u r n c o d e   & " .   M o v e   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   M o v e   - >   " &   r e t u r n c o d e   & " .   M o v e   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   m o v e D e l a y / m o v e D e l a y S t a r t   c o m m a n d .   "  
 	 n o t e   " S t a r t   a   l o g   b e f o r e   t h e   P L A   m o v e   t o   3 0 "  
  
 ' *   T e s t   A u t o T h r o t t l e   M o v e D e l a y   C o m m a n d  
 	 r e t u r n c o d e   =   a t _ m o v e D e l a y   ( " T L A " ,   3 0 ,   0 . 5 ,   1 )  
 ' 	 r e t u r n c o d e   =   a t _ m o v e D e l a y   ( " N 1 " ,   1 9 5 0 ,   5 ,   1 )  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   M o v e D e l a y   - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   M o v e D e l a y   - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
 	  
 	 s t a r t _ l o g   " A u t o T h r o t t l e M K I I I " ,   " M o v e D e l a y S t a r t   t e s t "  
 	 d e l a y   1 0  
 	 S t o p _ l o g   " A u t o T h r o t t l e M K I I I "  
 ' *   T e s t   A u t o T h r o t t l e   M o v e D e l a y S t a r t   C o m m a n d  
   	 r e t u r n c o d e   =   a t _ m o v e D e l a y S t a r t   ( 1 0 ,   1 5 )  
  
   	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   M o v e D e l a y S t a r t   - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y S t a r t   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   M o v e D e l a y S t a r t   - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y S t a r t   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
  
 ' *   T e s t   A u t o T h r o t t l e   S e t C h a n n e l   C o m m a n d  
 ' *   S e t C h a n n e l   a l l o w s   t o   s e t   a n y   t a g   i n s i d e   t h e   P L A .   P l e a s e   n o t e   t h e   s e t c h a n n e l   v a l u e   s h o u l d   b e   t h e   c h a n n e l   a l i a s   i n s t e a d   o f   P L C   t a g .  
 ' *   A l s o ,   o n l y   t h e   p r e - d e f i n e d   s e t c h a n n e l   a l i a s   w i l l   b e   a v a i l a b l e   f o r   t h e   T P .   T h e   s e t c h a n n e l   a l i a s   c o u l d   b e   f o u n d   a t   T h r o t t l e   c o n f i g   f i l e .  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   S e t C h a n n e l   c o m m a n d .   "  
 	 n o t e   " S e t   t h e   F u e l   b u t t o n   O n   t h e   T h r o t t l e   G U I   f r o m   0   t o   1 "  
 	 s e t v a l u e   =   0  
 	 r e t u r n c o d e   =   a t _ S e t C h a n n e l   ( " r e m F u e l O n " ,   s e t v a l u e )  
 	  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   S e t C h a n n e l   F u e l   t o   O f f   i s   - >   " &   r e t u r n c o d e   & " .   S e t C h a n n e l   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   S e t c h a n n e l   F u e l   t o   O f f   i s     - >   " &   r e t u r n c o d e   & " .   S e t C h a n n e l   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	 d e l a y   2  
  
 	 s e t v a l u e   =   1  
 	 r e t u r n c o d e   =   a t _ S e t C h a n n e l   ( " r e m F u e l O n " ,   s e t v a l u e )  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   S e t c h a n n e l   F u e l   t o   O n   i s   - >   " &   r e t u r n c o d e   & " .   S e t C h a n n e l   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   S e t c h a n n e l   F u e l   t o   O n   i s     - >   " &   r e t u r n c o d e   & " .   S e t C h a n n e l   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 ' *   T e s t   A u t o T h r o t t l e   M o v e A s y n c   C o m m a n d  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   m o v e A s y n c   c o m m a n d .   "  
 	 n o t e   " M o v e   t h e   P L A   t o   4 0   d e g r e e   a n d   T a k e   a   l o g   a t   t h e   s a m e   t i m e   i f   F u e l   i s   O n   b y   u s i n g   m o v e A s y n c "  
 	 r e t u r n c o d e   =   a t _ m o v e A s y n c   ( " T L A " ,   4 0 ,   1 0 ,   1 4 . 0 ,   0 . 5 ,   1 . 0 )  
 ' 	 r e t u r n c o d e   =   a t _ m o v e A s y n c   ( " N 1 " ,   2 6 0 0 ,   1 0 ,   1 4 . 0 ,   5 ,   1 . 0 )  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   T L A   M o v e A s y n c   i s   - >   " &   r e t u r n c o d e   & " .   M o v e A s y n c   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   T L A   M o v e A s y n c   i s     - >   " &   r e t u r n c o d e   & " .   M o v e A s y n c   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
 	 	  
 	 i f   c v _ F u e l O n   =   1   T h e n  
 	 	 s t a r t _ l o g   " A u t o T h r o t t l e M K I I I " ,   " M o v e A s y n c   c o m m a n d   t e s t "  
 	 	 d e l a y   1 0  
 	 	 S t o p _ l o g   " A u t o T h r o t t l e M K I I I "  
 	 e n d   i f  
  
 ' *   T e s t   M o v e D e l a y S t a r t A s y n c   C o m m a n d  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   m o v e D e l a y S t a r t A s y n c   c o m m a n d .   "  
 	 n o t e   " T a k e   a   l o g   b e f o r e   t h e   P L A   m o v e   t o   4 5 .   A f t e r   t h e   l o g   P L A   w i l l   m o v e   t o   4 5   a n d   a t   t h e   s a m e   t i m e   d o   a   f u l l s e t "  
 	 r e t u r n c o d e   =   a t _ m o v e D e l a y   ( " T L A " ,   4 5 ,   0 . 5 ,   1 )  
 ' 	 r e t u r n c o d e   =   a t _ m o v e D e l a y   ( " N 1 " ,   2 9 2 5 ,   5 ,   1 )  
 	  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   M o v e D e l a y   i s   - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   M o v e D e l a y   i s     - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	 s t a r t _ l o g   " A u t o T h r o t t l e M K I I I " ,   " m o v e _ d e l a y _ A s y n c   c o m m a n d   t e s t "  
 	 d e l a y   1 0  
 	 S t o p _ l o g   " A u t o T h r o t t l e M K I I I "  
 	 r e t u r n c o d e   =   a t _ m o v e D e l a y S t a r t A s y n c   ( 1 0 ,   1 5 )  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   M o v e D e l a y S t a r t A s y n c   i s   - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y S t a r t A s y n c   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   M o v e D e l a y S t a r t A s y n c   i s     - >   " &   r e t u r n c o d e   & " .   M o v e D e l a y S t a r t A s y n c   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	 d o _ f u l l s e t   1 0 ,   " M o v e D e l a y S t a r t A s y n c " ,   " M o v e D e l a y S t a r t A s y n c t e s t "  
  
 ' 	 d e l a y   5  
  
  
 ' *   T e s t   A u t o T h r o t t l e   P a u s e   &   C o n t i n u e   C o m m a n d    
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   P a u s e / C o n t i n u e   c o m m a n d . "  
 	 n o t e   " M o v e   t h e   P L A   t o   6 0   d e g r e e .   P a u s e   a t   5 5 d e g r e e   a n d   t a k e   a   l o g   p a u s e _ t e s t .   C o n t i n u e   a f t e r   t h e   l o g   f i n i s h e d . "  
 	 r e t u r n c o d e   =   a t _ m o v e A s y n c   ( " T L A " ,   6 0 ,   3 0 ,   7 0 ,   0 . 5 ,   1 . 0 )  
 ' 	 r e t u r n c o d e   =   a t _ m o v e A s y n c   ( " N 1 " ,   3 9 0 0 ,   3 0 ,   7 0 ,   5 ,   1 . 0 )  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   m o v e A s y n c   i s   - >   " &   r e t u r n c o d e   & " .   m o v e A s y n c   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   m o v e A s y n c   i s     - >   " &   r e t u r n c o d e   & " .   m o v e A s y n c   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	 w a i t   " P L A   =   5 5 " ,   3 0 ,   0 . 1 ,   ,   ,   ,   S K I P ,   "   P L A   D i d   n o t   r e a c h   5 5 "  
 ' 	 w a i t   " N 1   =   3 5 7 5 " ,   3 0 ,   5 ,   ,   ,   ,   S K I P ,   "   N 1   D i d   n o t   r e a c h   3 5 7 5 "  
  
 	 r e s u l t   " c v _ P L A   "   &   c v _ P L A  
  
 	 i f   c v _ P L A   >   5 4 . 5   a n d   c v _ P L A   <   5 5   T h e n  
 ' 	 i f   c v _ N 1   >   3 5 7 3   a n d   c v _ P L A   <   3 5 7 7   T h e n  
 	 	 r e t u r n c o d e   =   a t _ P a u s e  
 	 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 	 r e s u l t   " r e t u r n c o d e   f o r   P a u s e   i s   - >   " &   r e t u r n c o d e   & " .   P a u s e   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 	 E l s e  
 	 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   P a u s e   i s     - >   " &   r e t u r n c o d e   & " .   P a u s e   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 	 E n d   i f  
  
 	 	 s t a r t _ l o g   " A u t o T h r o t t l e M K I I I " ,   " p a u s e _ t e s t "  
 	 	 d e l a y   1 3 ,   " P a u s e   a n d   w a i t i n g   f o r   t h e   l o g   f i n i s h e d "  
 	 e n d   i f  
 	 	 r e t u r n c o d e   =   a t _ C o n t i n u e  
  
 	 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 	 r e s u l t   " r e t u r n c o d e   f o r   C o n t i n u e   i s   - >   " &   r e t u r n c o d e   & " .   C o n t i n u e   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 	 E l s e  
 	 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   C o n t i n u e   i s     - >   " &   r e t u r n c o d e   & " .   C o n t i n u e   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 	 E n d   i f  
  
 	 	 d e l a y   1 0 ,   " w a i t   t h e   P L A   m o v e   t o   6 0 "  
  
 ' *   T e s t   A u t o T h r o t t l e   G e t S t a t u s   C o m m a n d  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   G e t S t a t u s   C o m m a n d . "  
 	 n o t e   " G e t   t h e   s t a t u s   o f   t h e   t h r o t t l e   s y s t e m . "  
 	 	  
 	 r e t u r n c o d e   =   a t _ G e t S t a t u s  
 	 r e s u l t   " r e t u r n c o d e   f o r   G e s t S t a t u s   - >   " &   r e t u r n c o d e   & " " ,   R E P O R T   &   " T h r o t t l e "  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 	 r e s u l t   " F a i l e d   t o   r e t r i v e   t h e   s t a t u s "  
 	 	 d e l a y   3  
   	 E n d   i f  
  
 	 i f   r e t u r n c o d e   =   1   T h e n  
 	 	 r e s u l t   " S y s t e m   i s   i n   m a n u a l   m o d e "  
 	 	 d e l a y   3  
 	 E n d   i f  
  
 	 i f   r e t u r n c o d e   =   2   T h e n  
 	 	 r e s u l t   " S y s t e m   i s   i n   A u t o   M o d e ,   L e v e r   i s   n o t   m o v i n g "  
 	 	 d e l a y   3  
 	 E n d   i f  
  
 	 i f   r e t u r n c o d e   =   3   T h e n  
 	 	 r e s u l t   " S y s t e m   i s   i n   A u t o   M o d e ,   R i g h t   L e v e r   i s   n o t   m o v i n g "  
 	 	 d e l a y   3  
 	 E n d   i f  
  
 	 i f   r e t u r n c o d e   =   4   T h e n  
 	 	 r e s u l t   " S y s t e m   i s   i n   A u t o   M o d e ,   L e f t   L e v e r   i s   n o t   m o v i n g "  
 	 	 d e l a y   3  
 	 E n d   i f  
  
 	 i f   r e t u r n c o d e   =   5   T h e n  
 	 	 r e s u l t   " S y s t e m   i s   i n   A u t o   M o d e ,   B o t h   L e v e r s   a r e   m o v i n g "  
 	 	 d e l a y   3  
 	 E n d   i f    
 	 	 	 	 	 	  
 	 i f   r e t u r n c o d e   =   6   T h e n  
 	 	 r e s u l t   " S y s t e m   i s   i n   A u t o   M o d e ,   m o v e m e n t   i s   p a u s e d "  
 	 	 d e l a y   3  
 	 E n d   i f  
    
 ' *   T e s t   A u t o T h r o t t l e   G e t C h a n n e l   C o m m a n d .   G e t C h a n n e l   n a m e   s h o u l d   b e   P L C   t a g   n a m e .  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   G e t _ C h a n n e l   C o m m a n d "  
 	 n o t e   " G e t   t h e   c u r r e n t   P L A   r e a d i n g . "  
  
 	 r e t u r n c o d e   =   a t _ G e t C h a n n e l   ( " O _ C u r r e n t A c t u a t o r 1 P o s i t i o n _ R e a l " ,   r e t V a l u e )  
 	 r e s u l t   " G e t   C h a n n e l   P L A   i s   n o w   - >   " &   r e t V a l u e   & " " ,   R E P O R T   &   " T h r o t t l e "  
 	  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   G e t c h a n n e l   i s   - >   " &   r e t u r n c o d e   & " .   G e t c h a n n e l   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   G e t c h a n n e l   i s     - >   " &   r e t u r n c o d e   & " .   G e t c h a n n e l   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
 	  
 	 i n s t r u c t i o n   " M o v e   t h e   P L A   t o   9 0   d e g r e e "  
 	 r e t u r n c o d e   =   a t _ M o v e   ( " T L A " ,   9 0 ,   5 ,   7 . 0 ,   0 . 5 ,   1 . 0 )  
  
  
 ' *   T e s t   A u t o T h r o t t l e   S e t O p e n L o o p M o d e   C o m m a n d  
 	 i n s t r u c t i o n   " T e s t   A u t o   T h r o t t l e   S e t O p e n L o o p / S e t C l o s e d L o o p   c o m m a n d "  
 	 n o t e   " T a k e   a   f u l l s e t   a f t e r   T h r o t t l e   s e t   t o   O p e n   l o o p "  
 	 r e t u r n c o d e   =   a t _ S e t O p e n L o o p M o d e  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   S e t O p e n L o o p M o d e   i s   - >   " &   r e t u r n c o d e   & " .   S e t O p e n L o o p M o d e   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   S e t O p e n L o o p M o d e   i s     - >   " &   r e t u r n c o d e   & " .   S e t O p e n L o o p M o d e   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	 d o _ f u l l s e t   1 0 ,   " O p e n L o o p L o g " ,   " O p e n L o o p L o g "  
 	  
 ' *   T e s t   A u t o T h r o t t l e   S e t C l o s e d L o o p M o d e   C o m m a n d  
 	 r e t u r n c o d e   =   a t _ S e t C l o s e d L o o p M o d e  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   S e t C l o s e d L o o p M o d e   i s   - >   " &   r e t u r n c o d e   & " .   S e t C l o s e d L o o p M o d e   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   S e t C l o s e d L o o p M o d e   i s     - >   " &   r e t u r n c o d e   & " .   S e t C l o s e d L o o p M o d e   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
 	  
 	 i n s t r u c t i o n   " M o v e   t h e   P L A   t o   6 0   d e g r e e "  
 	 r e t u r n c o d e   =   a t _ M o v e   ( " T L A " ,   6 0 ,   5 ,   7 . 0 ,   0 . 5 ,   1 . 0 )  
  
  
 	 i n s t r u c t i o n   " M o v e   t h e   P L A   t o   0   d e g r e e "  
 	 r e t u r n c o d e   =   a t _ M o v e   ( " T L A " ,   0 ,   5 ,   7 . 0 ,   0 . 5 ,   1 . 0 )  
  
 	  
 ' *   C h a n g e   t h e   S e t C h a n n e l   b a c k   t o   t h e   o r i g i n a l   c o n d i t i o n  
 	 i n s t r u c t i o n   " R e s e t   t h e   S e t C h a n n e l   b a c k   t o   t h e   o r i g i n a l   c o n d i t i o n .   "  
 	 n o t e   " S e t   t h e   F u e l   b u t t o n   O n   t h e   T h r o t t l e   G U I   f r o m   1   t o   0 "  
 	 s e t v a l u e   =   0  
 	 r e t u r n c o d e   =   a t _ S e t C h a n n e l   ( " r e m F u e l O n " ,   s e t v a l u e )  
 	  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   S e t C h a n n e l   F u e l   t o   O f f   i s   - >   " &   r e t u r n c o d e   & " .   S e t C h a n n e l   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   S e t c h a n n e l   F u e l   t o   O f f   i s     - >   " &   r e t u r n c o d e   & " .   S e t C h a n n e l   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 	  
 ' *   T e s t   A u t o T h r o t t l e   S t o p   C o m m a n d  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   S t o p   c o m m a n d . "  
 	 n o t e   " T h e   R e m o t e   C o n t r o l   o n   t h e   T h r o t t l e   G U I   s h o u l d   g o n e "  
 	 r e t u r n c o d e   =   a t _ s t o p a u t o m o d e  
 	 r e s u l t   " r e t u r n c o d e   f o r   S t o p A u t o M o d e   - >   " &   r e t u r n c o d e   & " " ,   R E P O R T   &   " T h r o t t l e "  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 	 r e s u l t   " A u t o   m i s s i o n   i s   c o m p l e t e d . "  
 	 e n d   i f  
 e l s e  
 	 r e s u l t   " E r r o r !   R e t u r n c o d e   - >   " &   r e t u r n c o d e   & "   o c c u r r e d   i n   S t a r t   A u t o   M o d e " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 e n d   i f  
  
 ' * - - - - - - - - - - - - - - - - - - - - - - - - - - T e s t   A b o r t   c o m m a n d - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
 i n s t r u c t i o n   " P u t   t h r o t t l e   i n t o   a u t o   m o d e   a g a i n   f o r   A b o r t   c o m m a n d   t e s t . "  
 r e t u r n c o d e   =   a t _ s t a r t a u t o m o d e  
 r e s u l t   " r e t u r n c o d e   f o r   s t a r t a u t o m o d e   - >   " &   r e t u r n c o d e   & " " ,   R E P O R T   &   " T h r o t t l e "  
  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 	 r e s u l t   " A u t o   m i s s i o n   s t a r t   a g a i n . "  
 	 e n d   i f  
  
 i f   r e t u r n c o d e   =   0   T h e n  
  
 	 i n s t r u c t i o n   " T e s t   A u t o T h r o t t l e   A b o r t   c o m m a n d . "  
 	 n o t e   " M o v e   t h e   P L A   t o   2 0   d e g r e e   t h e n   a b o r t "  
 	 r e t u r n c o d e   =   a t _ M o v e   ( " T L A " ,   2 0 ,   5 ,   7 . 0 ,   0 . 5 ,   1 . 0 )  
 ' 	 r e t u r n c o d e   =   a t _ M o v e   ( " N 1 " ,   1 3 0 0 ,   5 ,   7 . 0 ,   5 ,   1 . 0 )  
 	  
 	 r e t u r n c o d e   =   a t _ A b o r t M o v e  
 	  
 	 i f   r e t u r n c o d e   =   0   T h e n  
 	 r e s u l t   " r e t u r n c o d e   f o r   A b o r t M o v e   i s   - >   " &   r e t u r n c o d e   & " .   A b o r t M o v e   c o m m a n d   s u c c e e d e d " ,   R E P O R T   &   " T h r o t t l e "  
 	 E l s e  
 	 r e s u l t   " C a u t i o u s !   r e t u r n c o d e   f o r   A b o r t M o v e   i s     - >   " &   r e t u r n c o d e   & " .   A b o r t M o v e   c o m m a n d   n o t   s u c c e e d e d .   " ,   R E P O R T   &   " T h r o t t l e " ,   R E D  
 	 E n d   i f  
  
 e l s e  
 	 r e s u l t   " E r r o r !     R e t u r n c o d e   - >   " &   r e t u r n c o d e   & "   o c c u r r e d   i n   S t a r t   A u t o   M o d e "  
 e n d   i f  
 