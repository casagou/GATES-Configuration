O p t i o n   E x p l i c i t  
  
 ' *   < s c r i p t . t p s >  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' *     A U T H O R :   < y o u r   n a m e   g o e s   h e r e >  
 ' *  
 ' *     D E S C R I P T I O N :  
 ' *     T e s t   P r e p a r a t i o n  
 ' *  
 ' *     D A T E :   9 / 1 5 / 2 0 0 5   8 : 1 8 : 1 5   A M  
 ' *  
 ' *     M O D I F I C A T I O N S :  
 ' *         D A T E                   W H O     N C R         D E S C R I P T I O N  
 ' *         - - - - - - - - - -       - - -     - - - - -     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
 ' *     V 1 . 0 5     1 9 / 1 0 / 0 5       D P     C o r r e c t e d   s e t   t o   m a n u a l   s t a r t  
 ' *     V 1 . 0 4     1 9 / 1 0 / 0 5       D P     T e s t i n g   e r r o r s  
 ' *     V 1 . 0 3     1 5 / 0 9 / 0 5       J C     C o n v e r t e d   t o   p h a s e   3   l a n g u a g e  
 ' *     V 1 . 0 2   0 9 / 0 7 / 2 0 0 4     D P     M o d i f i e d   f o r   D e m o .     A d d e d   s e t _ c h a n n e l s   f o r   E N G M O D   a n d   C 4  
 ' *     V 1 . 0 1   0 7 / 0 9 / 2 0 0 1     R H     I n i t i a l  
 ' *                                                 s i n c e   t h e   T I P   i s   n o t   w o r k i n g   r i g h t   n o w .  
 ' *     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ' *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 '   * * * * *   L O C A L   V A R I A B L E   D E C L A R A T I O N S   * * * * *  
 D i m   l v I D G d i s c ,   l v I D G i n s t ,   l v N o 1 I G N ,   l v N o 2 I G N ,   l v O i l L e v e l  
 D i m   l v P r e F u e l ,   l v P r e H r ,   l v P r e M i n ,   l v S t a r t l e a k ,   t e m p v a r 1 g v    
  
 '   C h a n n e l   R e g i s t r a t i o n  
 c h a n n e l   " E n g _ O n ,   P r e R T M i n ,   P r e R T H r ,   P r e F u e l ,   I D G D i s c ,   I D G D i s c S T ,   F u e l O n S ,   N o r m a l ,   M o d e P o s n ,   S t M o d e ,   S t M o d e S T ,   I g n S t a r t ,   F u e l O f f F B ,   E N G M O D ,   C 4 , E N A B L E _ A L A R M S ,   S t a r t M o d e "  
  
 s e t _ c h a n n e l   E N A B L E _ A L A R M S ,   1  
 s e t _ c h a n n e l   E N G M O D ,   1  
 s e t _ c h a n n e l   C 4 ,   1  
 t e m p v a r 1 g v   =   0  
 I f   c v _ E n g _ O n   =   1   T h e n  
 q u i t  
 E n d   I f  
  
 p r o m p t _ n u m   " E n t e r   p r e v i o u s   r u n   t i m e :   H o u r s " ,   l v P r e H r ,   0 ,   1 0 0 ,   1  
 s e t _ c h a n n e l   P r e R T H r ,   l v P r e H r  
 p r o m p t _ n u m   " E n t e r   p r e v i o u s   r u n   t i m e :   M i n u t e s " ,   l v P r e M i n ,   0 ,   6 0 , 1 0  
 s e t _ c h a n n e l   P r e R T M i n ,   l v P r e M i n  
 p r o m p t _ n u m   " E n t e r   t h e   a m o u n t   o f   f u e l   u s e d   f o r   p r e v i o u s   r u n   i n   l i t r e s " ,   l v P r e F u e l ,   0 ,   1 0 0 0 0 0 ,   5 5  
 s e t _ c h a n n e l   P r e F u e l ,   l v P r e F u e l  
  
 p r o m p t _ b o o   " I s   t h e   I D G   i n s t a l l e d ? " ,   l v I D G i n s t  
  
 I f   l v I D G i n s t   =   T R U E   T h e n  
 r e s u l t   " E n t e r   t h e   I D G   I n s t a l l e d   l o g i c "  
 i n s t r u c t i o n   " C h e c k   I D G   d i s c o n n e c t   o r   p r e s s   S K I P " ,   S K I P  
 I f   s k i p g v   =   F A L S E   T h e n  
 s e t _ c h a n n e l   I D G D i s c ,   1  
 w a i t   " I D G D i s c S T   =   1 " ,   3 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " I D G   d i s c o n n e c t   f a i l e d .   U s e   P L C . "  
 p r o m p t _ b o o   " W a s   I D G   d i s c o n n e c t   s a t i s f a c t o r y ? " ,   l v I D G d i s c  
 I f   l v I D G d i s c   =   T R U E   T h e n  
 r e s u l t   " I D G   d i s c o n n e c t   o p e r a t i o n   O K " ,   R E P O R T   &   " I D G d i s c "  
 E l s e  
 r e s u l t   " I D G   d i s c o n n e c t   o p e r a t i o n   N O T   O K " ,   R E P O R T   &   " I D G d i s c "  
 E n d   I f  
 s e t _ c h a n n e l   I D G D i s c ,   0  
 w a i t   " I D G D i s c S T   =   0 " ,   3 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " I D G   d i s c o n n e c t   f a i l e d .   U s e   P L C . "  
 E n d   I f  
 '   *   V 1 . 0 3     A d d e d   t h e   E l s e   f o r   t e s t i n g  
 E l s e  
 r e s u l t   " E n t e r   t h e   I D G   N o t   I n s t a l l e d   l o g i c "  
 E n d   I f  
  
 i n s t r u c t i o n   " D o   I g n i t i o n   C h e c k "  
  
 i n s t r u c t i o n   " 5 . J . ( 1 ) ( a )   S e t   f u e l   s e l e c t   s w i t c h   t o   C U T O F F   p o s i t i o n "  
 '   *   D P P   w a i t   " F u e l O n S   =   0 " ,   1 0 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " F u e l   s e l e c t   s w i t c h   n o t   i n   C u t o f f   p o s i t i o n   a f t e r   1 0   s . "  
 w a i t   " F u e l O n S   =   0 " ,   1 0 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " F u e l   s e l e c t   s w i t c h   n o t   i n   C u t o f f   p o s i t i o n   a f t e r   1 0   s . "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   f u e l   s e l e c t   s w i t c h   C u t o f f   c h e c k . "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 1 ) ( b )   S e t   T h r o t t l e   t o   G I "  
  
 i n s t r u c t i o n   " 5 . J . ( 1 ) ( c )   S e t   M o d e   S e l e c t o r   t o   N O R M A L "  
 I f   c v _ M o d e P o s n   < >   2   T h e n  
 s e t _ c h a n n e l   N o r m a l ,   1  
 w a i t   " M o d e P o s n   =   2 " ,   3 ,   0 . 1 , , , , , ,   M S G ,     " M o d e   S e l e c t o r   S w i t c h   n o t   r e s p o n d i n g .     U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   M o d e   S e l e c t o r   t o   N O R M A L "  
 E l s e  
 r e s u l t   " M o d e   S e l e c t o r   S w i t c h   s e l e c t e d   t o   N O R M A L "  
 E n d   I f  
 E l s e  
 r e s u l t   " M o d e   S e l e c t o r   S w i t c h   w a s   a l r e a d y   i n   N O R M A L   p o s i t i o n "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 1 ) ( e )   M a k e   s u r e   t h e r e   i s   n o   s t a r t e r   i n l e t   a i r   p r e s s u r e "  
 n o t e   " T h e   e n g i n e   w i l l   n o t   b e   m o t o r e d   d u r i n g   t h i s   t e s t . "  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( a )   T u r n   o f f   t h e   1 1 5 V A C   i g n i t i o n   p o w e r   t o   E C U   B   c h a n n e l ,   "  
 n o t e   " o r   d i s c o n n e c t   t h e   J 2   h a r n e s s   f r o m   t h e   E C U . "  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( b )   S e t   t h e   M a n u a l   S t a r t   s w i t c h   t o   O N "  
 ' *   V 1 . 0 5   s e t _ c h a n n e l   S t M o d e ,   1  
 s e t _ c h a n n e l   S t a r t M o d e ,   1  
 w a i t   " S t M o d e S T   =   1 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " S t a r t   M o d e   s w i t c h   n o t   r e s p o n d i n g .   U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   S t a r t   M o d e   M A N U A L   i n s t r u c t i o n . " ,   R E P O R T   &   " P r e T e s t "  
 E l s e  
 r e s u l t   " S t a r t   M o d e   s e t   t o   M A N U A L " ,   R E P O R T   &   " P r e T e s t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( c )   S e t   t h e   M o d e   S e l e c t o r   s w i t c h   t o   I G N I T I O N "  
 s e t _ c h a n n e l   I g n S t a r t ,   1  
 s e t _ c h a n n e l   N o r m a l ,   0  
 w a i t   " M o d e P o s n   =   3 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " M o d e   S e l e c t o r   S w i t c h   n o t   r e s p o n d i n g .     U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   M o d e   S e l e c t o r   S w i t c h   I G N I T I O N   i n s t r u c t i o n " ,   R E P O R T   &   " P r e T e s t "  
 E l s e  
 r e s u l t   " M o d e   S e l e c t o r   S w i t c h   s e l e c t e d   t o   I G N I T I O N " ,   R E P O R T   &   " P r e T e s t "  
 E n d   I f  
  
 i n s t r u c t i o n   " S e t   F u e l   t o   O N "  
 w a i t   " F u e l O f f F B   =   0 " ,   3 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " F u e l   n o t   O N "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   F u e l   O N   i n s t r u c t i o n " ,   R E P O R T   &   " M a n S t a r t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( d )   M a k e   s u r e   t h e   N o .   1   i g n i t i o n   s y s t e m   ( l e f t   h a n d   s i d e ) "  
 n o t e   " i s   f i r i n g .     L i s t e n   f o r   a n   a u d i b l e   c h e c k   i n   t h e   c e l l . "  
  
 p r o m p t _ b o o   " W a s   N o .   1   I g n i t o r   o p e r a t i o n   s a t i s f a c t o r y ? " ,   l v N o 1 I G N  
 I f   l v N o 1 I G N   =   T R U E   T h e n  
 r e s u l t   " N o .   1   I g n i t o r   o p e r a t i o n   O K " ,   R E P O R T   &   " N O 1 I G N I T "  
 E l s e  
 r e s u l t   " N o .   1   I g n i t o r   o p e r a t i o n   N O T   O K " ,   R E P O R T   &   " N O 1 I G N I T "  
 E n d   I f  
  
 i n s t r u c t i o n   " S e t   F u e l   t o   O F F "  
 w a i t   " F u e l O f f F B   =   1 " ,   3 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " F u e l   n o t   O F F "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   F u e l   O F F   i n s t r u c t i o n " ,   R E P O R T   &   " M a n S t a r t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( e )   S e t   t h e   M a n u a l   S t a r t   s w i t c h   t o   O F F "  
 ' *   V 1 . 0 5   s e t _ c h a n n e l   S t M o d e ,   0  
 s e t _ c h a n n e l   S t a r t M o d e ,   0  
 w a i t   " S t M o d e S T   =   0 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " S t a r t   M o d e   s w i t c h   n o t   r e s p o n d i n g .   U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   S t a r t   M o d e   M A N U A L   O F F   i n s t r u c t i o n . " ,   R E P O R T   &   " P r e T e s t "  
 E l s e  
 r e s u l t   " S t a r t   M o d e   s e t   t o   M A N U A L " ,   R E P O R T   &   " P r e T e s t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( f )   S e t   t h e   M o d e   S e l e c t o r   t o   N O R M A L "  
 s e t _ c h a n n e l   N o r m a l ,   1  
 w a i t   " M o d e P o s n   =   2 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " M o d e   S e l e c t o r   S w i t c h   n o t   r e s p o n d i n g .     U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   M o d e   S e l e c t o r   t o   N O R M A L "  
 E l s e  
 r e s u l t   " M o d e   S e l e c t o r   S w i t c h   s e l e c t e d   t o   N O R M A L "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( g ) 1   T u r n   o n   t h e   1 1 5 V A C   i g n i t i o n   p o w e r   t o   E C U   B   c h a n n e l ,   "  
 n o t e   " o r   c o n n e c t   t h e   J 2   h a r n e s s   t o   t h e   E C U . "  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( g ) 2   T u r n   o f f   t h e   1 1 5 V A C   i g n i t i o n   p o w e r   t o   E C U   A   c h a n n e l ,   "  
 n o t e   " o r   d i s c o n n e c t   t h e   J 1   h a r n e s s   f r o m   t h e   E C U . "  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( h )   S e t   t h e   M a n u a l   S t a r t   s w i t c h   t o   O N "  
 ' *   V 1 . 0 5   s e t _ c h a n n e l   S t M o d e ,   1  
 s e t _ c h a n n e l   S t a r t M o d e ,   1  
 w a i t   " S t M o d e S T   =   1 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " S t a r t   M o d e   s w i t c h   n o t   r e s p o n d i n g .   U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   S t a r t   M o d e   M A N U A L   i n s t r u c t i o n . " ,   R E P O R T   &   " P r e T e s t "  
 E l s e  
 r e s u l t   " S t a r t   M o d e   s e t   t o   M A N U A L " ,   R E P O R T   &   " P r e T e s t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( i )   S e t   t h e   M o d e   S e l e c t o r   s w i t c h   t o   I G N I T I O N "  
 s e t _ c h a n n e l   I g n S t a r t ,   1  
 s e t _ c h a n n e l   N o r m a l ,   0  
 w a i t   " M o d e P o s n   =   3 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " M o d e   S e l e c t o r   S w i t c h   n o t   r e s p o n d i n g .     U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   M o d e   S e l e c t o r   S w i t c h   I G N I T I O N   i n s t r u c t i o n " ,   R E P O R T   &   " P r e T e s t "  
 E l s e  
 r e s u l t   " M o d e   S e l e c t o r   S w i t c h   s e l e c t e d   t o   I G N I T I O N " ,   R E P O R T   &   " P r e T e s t "  
 E n d   I f  
  
 i n s t r u c t i o n   " S e t   F u e l   t o   O N "  
 w a i t   " F u e l O f f F B   =   0 " ,   3 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " F u e l   n o t   O N "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   F u e l   O N   i n s t r u c t i o n " ,   R E P O R T   &   " M a n S t a r t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( j )   M a k e   s u r e   t h e   N o .   2   i g n i t i o n   s y s t e m   ( r i g h t   h a n d   s i d e ) "  
 n o t e   " i s   f i r i n g .     L i s t e n   f o r   a n   a u d i b l e   c h e c k   i n   t h e   c e l l . "  
  
 p r o m p t _ b o o   " W a s   N o .   2   I g n i t o r   o p e r a t i o n   s a t i s f a c t o r y ? " ,   l v N o 2 I G N  
 I f   l v N o 2 I G N   =   1   T h e n  
 r e s u l t   " N o .   2   I g n i t o r   o p e r a t i o n   O K " ,   R E P O R T   &   " N O 2 I G N I T "  
 E l s e  
 r e s u l t   " N o .   2   I g n i t o r   o p e r a t i o n   N O T   O K " ,   R E P O R T   &   " N O 2 I G N I T "  
 E n d   I f  
  
 i n s t r u c t i o n   " S e t   F u e l   t o   O F F "  
 w a i t   " F u e l O f f F B   =   1 " ,   3 ,   0 . 1 ,   ,   ,   ,   ,   ,   M S G ,   " F u e l   n o t   O F F "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   F u e l   O F F   i n s t r u c t i o n " ,   R E P O R T   &   " M a n S t a r t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( k )   S e t   t h e   M a n u a l   S t a r t   s w i t c h   t o   O F F "  
 ' *   V 1 . 0 5   s e t _ c h a n n e l   S t M o d e ,   0  
 s e t _ c h a n n e l   S t a r t M o d e ,   0  
 w a i t   " S t M o d e S T   =   0 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " S t a r t   M o d e   s w i t c h   n o t   r e s p o n d i n g .   U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   S t a r t   M o d e   M A N U A L   O F F   i n s t r u c t i o n . " ,   R E P O R T   &   " P r e T e s t "  
 E l s e  
 r e s u l t   " S t a r t   M o d e   s e t   t o   M A N U A L " ,   R E P O R T   &   " P r e T e s t "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( l )   S e t   t h e   M o d e   S e l e c t o r   t o   N O R M A L "  
 s e t _ c h a n n e l   N o r m a l ,   1  
 w a i t   " M o d e P o s n   =   2 " ,   3 ,   0 . 1 , , , , , ,   M S G ,   " M o d e   S e l e c t o r   S w i t c h   n o t   r e s p o n d i n g .     U s e   P L C "  
 I f   s k i p g v   =   1   T h e n  
 r e s u l t   " O p e r a t o r   s k i p p e d   M o d e   S e l e c t o r   t o   N O R M A L "  
 E l s e  
 r e s u l t   " M o d e   S e l e c t o r   S w i t c h   s e l e c t e d   t o   N O R M A L "  
 E n d   I f  
  
 i n s t r u c t i o n   " 5 . J . ( 2 ) ( m )   T u r n   o n   t h e   1 1 5 V A C   i g n i t i o n   p o w e r   t o   E C U   A   c h a n n e l ,   "  
 n o t e   " o r   c o n n e c t   t h e   J 1   h a r n e s s   t o   t h e   E C U . "  
  
 i n s t r u c t i o n   " D o   a n   A i r   S y s t e m   l e a k c h e c k "  
 n o t e   " T u r n   T e s t   C e l l   s t a r t   a i r   O N "  
 n o t e   " C h e c k   f o r   a n y   a i r   l e a k s "  
 n o t e   " T u r n   T e s t   C e l l   s t a r t   a i r   O F F "  
 p r o m p t _ b o o   " W a s   a i r   l e a k   c h e c k   s a t i s f a c t o r y ? " ,   l v S t a r t l e a k  
 I f   l v S t a r t l e a k   =   T R U E   T h e n  
 r e s u l t   " S t a r t   a i r   l e a k   c h e c k   O K " ,   R E P O R T   &   " S t a r t l e a k "  
 E l s e  
 r e s u l t   " S t a r t   a i r   l e a k   c h e c k   N O T   O K " ,   R E P O R T   &   " S t a r t l e a k "  
 E n d   I f  
  
 i n s t r u c t i o n   " D o   a n   o i l   q u a n t i t y   c h e c k "  
 p r o m p t _ b o o   " I s   o i l   l e v e l   s a t i s f a c t o r y ? " ,   l v O i l L e v e l  
 I f   l v O i l L e v e l   =   T R U E   T h e n  
 r e s u l t   " O i l   l e v e l   O K " ,   R E P O R T   &   " O i l L e v e l "  
 E l s e  
 r e s u l t   " O i l   l e v e l   N O T   O K .     R e f i l l   o i l   t a n k " ,   R E P O R T   &   " O i l L e v e l "  
 E n d   I f  
  
 