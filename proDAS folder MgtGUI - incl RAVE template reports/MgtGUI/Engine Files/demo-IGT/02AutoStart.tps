O p t i o n   E x p l i c i t  
  
 ' *   < s c r i p t . t p s >  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' *     A U T H O R :   < J o a c h i m   A g o u >  
 ' *  
 ' *     D E S C R I P T I O N :  
 ' *     A u t o   S t a r t  
 ' *  
 ' *     D A T E :   2   D e c   2 0 1 6  
 ' *  
 ' *     M O D I F I C A T I O N S :  
 ' *         D A T E                           W H O     N C R         D E S C R I P T I O N  
 ' *         - - - - - - - - - - - - -       - - -     - - - - -     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
 ' *     V 0 . 1       2 D e c 2 0 1 6       J O A                     I n i t i a l  
 ' *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 '   C h a n n e l   R e g i s t r a t i o n  
 c h a n n e l   " S t a r t ,   F R ,   R W ,   P l a y ,   F W ,   R S ,   n _ G G ,   V _ G _ N ,   S t a r t ,   S h u t d o w n ,   T q _ P T _ ,   S o l _ F u e l _ ,   I g n i t i o n ,   N o S h u t d o w n ,   S t a r t R e s e t "  
  
 ' *     n o t e   1 0 0 %   N 2   =   1 4 4 6 0   r p m ;   1 0 0 %   N 1   =   4 7 8 4   r p m .  
 ' *       *     *  
 i n s t r u c t i o n   " R e s e t   s t a r t   c a l c u l a t i o n s "  
 s e t _ c h a n n e l   F R ,   0  
 s e t _ c h a n n e l   R W ,   0  
 s e t _ c h a n n e l   P l a y ,   0  
 s e t _ c h a n n e l   F W ,   0  
 s e t _ c h a n n e l   F W ,   0  
 s e t _ c h a n n e l   S t a r t ,   1  
 s e t _ c h a n n e l   S h u t d o w n ,   1  
  
 s e t _ c h a n n e l   R S ,   1  
 d e l a y   2  
 '   i n s t r u c t i o n   " s e t   _ R S   t o   0 "  
 s e t _ c h a n n e l   S h u t d o w n ,   0  
 s e t _ c h a n n e l   R S ,   0  
 s e t _ c h a n n e l   S t a r t ,   1  
  
 s e t _ c h a n n e l   S t a r t R e s e t ,   1    
 d e l a y   2  
 s e t _ c h a n n e l   S t a r t R e s e t ,   0  
  
 i n s t r u c t i o n   " S e t   G T   C o n t r o l l e r   S e t p o i n t   t o   z e r o "  
  
 i n s t r u c t i o n   " S e l e c t   R u n   E n a b l e d   M o d e   "  
 '   I f   c v _ M o d e P o s n   < >   2   T h e n  
 '   s e t _ c h a n n e l   N o r m a l ,   1  
 '   w a i t   " M o d e P o s n   =   2 " ,   3 ,   0 . 1 , , , , , ,   M S G ,     " M o d e   S e l e c t o r   S w i t c h   n o t   r e s p o n d i n g .     U s e   P L C "  
 '   I f   s k i p g v   =   1   T h e n  
 '   r e s u l t   " O p e r a t o r   s k i p p e d   M o d e   S e l e c t o r   t o   N O R M A L "  
 '   E l s e  
 '   r e s u l t   " M o d e   S e l e c t o r   S w i t c h   s e l e c t e d   t o   N O R M A L "  
 '   E n d   I f  
 '   E l s e  
 '   r e s u l t   " M o d e   S e l e c t o r   S w i t c h   w a s   a l r e a d y   i n   N O R M A L   p o s i t i o n "  
 '   E n d   I f  
 ' *     d e f i n e   a   S t a r t   l o g   w i t h :  
 ' *     E G T ,   W F M ,   W F M 1 ,   N 2 S ,   N 1 S ,   P O I L ,   T L A  
 s e t _ c h a n n e l   N o S h u t d o w n ,   1  
 s t a r t _ l o g   " S t a r t " ,   " S t a r t "  
 r e s u l t   " T r a n s i e n t   L o g   S t a r t   h a s   s t a r t e d . " ,   R E P O R T   &   " S t a r t " ,   B L U E  
  
 i n s t r u c t i o n   " S e l e c t   S p e e d   M o d e "  
 i n s t r u c t i o n   " S e l e c t   O p e r a t i o n   M o d e   t o   i n i t i a t e   S t a r t "  
 n o t e   " M o n i t o r   i n c r e a s i n g   G G   a n d   P T   o i l   p r e s s u r e s "  
 '   s e t _ c h a n n e l   S t a r t ,   1  
 '   d e l a y   2  
 s e t _ c h a n n e l   F W ,   1  
 w a i t   " n _ G G   > =   8 0 0 " ,   4 0 ,   4 5 0 , , , , , ,   M S G ,     " n _ G G   s l o w   t o   a c c e l e r a t e "  
 i n s t r u c t i o n   " S e l e c t   I g n i t i o n   M o d e "  
 c a u t i o n   " M o n i t o r   l i t e - o f f   a n d   s m o o t h ,   n _ G G   a n d   T _ 4   i n c r e a s e "  
 c a u t i o n   " I f   n _ G G   h a n g s ,   o r   T _ 4   i n c r e a s e s   t o o   r a p i d l y ,   s e l e c t   S H U T - D O W N "  
 s e t _ c h a n n e l   I g n i t i o n ,   1  
  
 '   w a i t   " E n d L i t e   =   1 " ,   2 0 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " N o   l i t e - o f f   a f t e r   2 0   s .   P r e s s   S K I P   t o   a b o r t   S t a r t "  
 '   I f   s k i p g v   =   T R U E   T h e n  
 '   r e s u l t   " S t a r t   a b o r t e d " ,   R E P O R T   &   " A u t o S t a r t "  
 ' *     q u i t  
 ' *     a u t o s t a r t   A b o r t S t a r t  
 '   E n d   I f  
  
 '   I f   c v _ t T o L i t e   >   1 5   T h e n  
 '   r e s u l t   " T i m e   t o   l i t e   i s   "   &   c v _ t T o L i t e   &   "   s   a n d   i t   s h o u l d   b e   1 5   s   m a x .   S t a r t   a b o r t e d " ,   R E P O R T   &   " A u t o S t a r t " ,   R E D  
 ' *     q u i t  
 ' *     a u t o s t a r t   A b o r t S t a r t  
 '   E n d   I f  
  
 i n s t r u c t i o n   " V e r i f y   s t a r t e r   c u t - o u t   a t   a p p r o x   4 9 0 0   r p m "  
 w a i t   " n _ G G   > =   4 8 0 0 " ,   4 0 ,   4 5 0 , , , , , ,   M S G ,     " n _ G G   s l o w   t o   a c c e l e r a t e "  
 w a i t   " n _ G G   > =   8 4 0 0 " ,   4 0 ,   4 5 0 , , , , , ,   M S G ,     " n _ G G   s l o w   t o   a c c e l e r a t e "  
 i n s t r u c t i o n   " V e r i f y   M a i n   G a s   F l o w   a t   a p p r o x   8 4 5 0   r p m "  
 w a i t   " n _ G G   > =   8 5 0 0 " ,   4 0 ,   4 5 0 , , , , , ,   M S G ,     " n _ G G   s l o w   t o   a c c e l e r a t e "  
 w a i t   " V _ G _ N   > =   2 0 " ,   4 ,   2 0 , , , , , ,   M S G ,     " N o   m a i n   g a s   f l o w ;   a b o r t   s t a r t "  
 r e s u l t   " M a i n   G a s   F l o w   d e t e c t e d " ,   R E P O R T   &   " S t a r t " ,   B L U E  
  
 '   w a i t   " E n d S t a r t L   =   1 " ,   1 2 0 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " E n d   S t a r t   i n d i c a t i o n   n o t   r e c e i v e d   i n   1 2 0   s "  
 '   I f   c v _ t T o I d l e   > =   1 2 0   T h e n  
 '   r e s u l t   " T i m e   f r o m   F u e l   O N   t o   I d l e   e x c e e d e d   1 2 0   s " ,   R E P O R T   &   " A u t o S t a r t " ,   R E D  
 '   E n d   I f  
  
 i n s t r u c t i o n   " V e r i f y   s t a b l e   i d l e "  
 i n s t r u c t i o n   " S e l e c t   I g n i t i o n   O f f "  
 s e t _ c h a n n e l   I g n i t i o n ,   0  
  
 s t o p _ l o g   " S t a r t "  
 i n s t r u c t i o n   " S t a b l i s e   a t   i d l e   f o r   5   m i n u t e s   t h e n   t a k e   a   F u l l s e t "  
 '   d e l a y   3 0 0  
 '   w a i t   t S t a b l e . . .    
 d e l a y   3 0  
 d o _ f u l l s e t   1 ,   " G r o u n d   I d l e   f o l l o w i n g   S t a r t " ,   " S t a r t "  
 s e t _ c h a n n e l   S o l _ F u e l _ ,   4 2 . 5  
 s e t _ c h a n n e l   T q _ P T _ ,   6 2 2 0  
 s e t _ c h a n n e l   P l a y ,   0  
 s e t _ c h a n n e l   F W ,   0  
 s e t _ c h a n n e l   S t a r t ,   0  
 