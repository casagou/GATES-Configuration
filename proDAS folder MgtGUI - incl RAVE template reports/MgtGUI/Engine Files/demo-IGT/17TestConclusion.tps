O p t i o n   E x p l i c i t  
  
 ' *   < s c r i p t . t p s >  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 ' *     A U T H O R :   D o n   P e r e i r a  
 ' *  
 ' *     D E S C R I P T I O N :  
 ' *     < d e s c r i b e   t h e   s c r i p t   h e r e >  
 ' *  
 ' *     D A T E :   9 / 1 5 / 2 0 0 5   8 : 4 8 : 5 7   A M  
 ' *  
 ' *     M O D I F I C A T I O N S :  
 ' *         D A T E                   W H O     N C R         D E S C R I P T I O N  
 ' *         - - - - - - - - - -       - - -     - - - - -     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
 ' *     V 1 . 0 1     1 1 / 0 9 / 2 0 0 1     R H       I n i t i a l  
 ' *     V 1 . 0 2     1 9 / 0 4 / 2 0 0 2     J N       A d d e d   i f   l o g i c   t o   c h e c k   i f   I D G   i n s t a l l e d  
 ' *     V 1 . 0 3     1 8 / 0 7 / 2 0 0 2     T C       R e m o v e d   r e f   t o f u e l   p r e s e r v a t i o n   s y s t e m   a n d   I D G   S c a v   f i l t e r  
 ' *     V 1 . 0 4     1 5 / 0 9 / 2 0 0 5     J C       C o n v e r t e d   t o   p h a s e   3   f o r m a t  
 ' *  
 ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
  
 '   * * * * *   L O C A L   V A R I A B L E   D E C L A R A T I O N S   * * * * *  
 D i m   C o n c l u d e ,   C S D F i l O K ,   E n g F i l I n s t ,   E n g F i l O K ,   E n g F u e l F i l O K  
 D i m   F u e l L k ,   I D G R e E n g ,   I n _ E x h O K ,   l v M C D O K ,   O i l L e v e l O K  
 D i m   O i l L k ,   R o t o r R o t ,   T e s t E q R e m  
  
 c h a n n e l   " E n g _ O n , I D G "  
  
 I f   c v _ E n g _ O n   =   1   T h e n  
 q u i t  
 E n d   I f  
  
 p r o m p t _ b o o   " D o   y o u   w a n t   t o   c o n c l u d e   t h i s   e n g i n e   t e s t ? " ,   C o n c l u d e  
 I f   C o n c l u d e   =   0   T h e n  
 q u i t  
 E n d   I f  
  
 i n s t r u c t i o n   " C h e c k   e n g i n e   f o r   l e a k s "  
 p r o m p t _ b o o   " A r e   t h e r e   f u e l   l e a k s ? " ,   F u e l L k  
 I f   F u e l L k   =   T R U E   T h e n  
 r e s u l t   " T h e r e   a r e   f u e l   l e a k s " ,   R E P O R T   &   " L e a k s C h e c k "  
 E l s e  
 r e s u l t   " T h e r e   a r e   n o   f u e l   l e a k s " ,   R E P O R T   &   " L e a k s C h e c k "  
 E n d   I f  
  
 p r o m p t _ b o o   " A r e   t h e r e   o i l   l e a k s ? " ,   O i l L k  
 I f   O i l L k   =   T R U E   T h e n  
 r e s u l t   " T h e r e   a r e   o i l   l e a k s " ,   R E P O R T   &   " L e a k s C h e c k "  
 E l s e  
 r e s u l t   " T h e r e   a r e   n o   o i l   l e a k s " ,   R E P O R T   &   " L e a k s C h e c k "  
 E n d   I f  
  
 i n s t r u c t i o n   " C h e c k   m a g n e t i c   c h i p   d e t e c t o r s "  
 p r o m p t _ b o o   " W e r e   a l l   M a g n e t i c   C h i p   D e t e c t o r s   O K   d u r i n g   t e s t ? " ,   l v M C D O K  
 I f   l v M C D O K   =   T R U E   T h e n  
 r e s u l t   " M a g n e t i c   C h i p   D e t e c t o r s   O K " ,   R E P O R T   &   " M C D C h e c k "  
 E l s e  
 r e s u l t   " M a g n e t i c   C h i p   D e t e c t o r s   N O T   O K " ,   R E P O R T   &   " M C D C h e c k "  
 E n d   I f  
  
 i n s t r u c t i o n   " C h e c k   e n g i n e   f u e l   f i l t e r "  
 p r o m p t _ b o o   " I s   e n g i n e   f u e l   f i l t e r   O K ? " ,   E n g F u e l F i l O K  
 I f   E n g F u e l F i l O K   =   T R U E   T h e n  
 r e s u l t   " E n g i n e   f u e l   f i l t e r   i s   O K " ,   R E P O R T   &   " F u e l F i l t e r C h k "  
 E l s e  
 r e s u l t   " E n g i n e   f u e l   f i l t e r   i s   n o t   O K " ,   R E P O R T   &   " F u e l F i l t e r C h k "  
 E n d   I f  
  
 i n s t r u c t i o n   " C h e c k   e n g i n e   o i l   f i l t e r "  
 p r o m p t _ b o o   " I s   e n g i n e   f i l t e r   O K ? " ,   E n g F i l O K  
 I f   E n g F i l O K   =   T R U E   T h e n  
 r e s u l t   " E n g i n e   f i l t e r   i s   O K " ,   R E P O R T   &   " O i l F i l t e r C h k "  
 E l s e  
 r e s u l t   " E n g i n e   f i l t e r   i s   n o t   O K " ,   R E P O R T   &   " O i l F i l t e r C h k "  
 E n d   I f  
  
 i n s t r u c t i o n   " I n s t a l l   n e w   e n g i n e   o i l   f i l t e r   i f   n e c e s s a r y "  
 p r o m p t _ b o o   " I s   e n g i n e   f i l t e r   i n s t a l l e d ? " ,   E n g F i l I n s t  
 I f   E n g F i l I n s t   =   T R U E   T h e n  
 r e s u l t   " N e w   e n g i n e   f i l t e r   i s   i n s t a l l e d " ,   R E P O R T   &   " N e w O i l F i l t e r "  
 E l s e  
 r e s u l t   " N e w   e n g i n e   f i l t e r   i s   n o t   i n s t a l l e d " ,   R E P O R T   &   " N e w O i l F i l t e r "  
 E n d   I f  
  
 ' *     V 1 . 0 2   a d d e d   i f   l o g i c   f o r   I D G  
 I f   c v _ I D G   =   1   T h e n  
 ' *     V 1 . 0 2   i n s t r u c t i o n   " C h e c k   I D G   o i l   f i l t e r "  
 i n s t r u c t i o n   " C h e c k   I D G   o i l   f i l t e r   i f   a p p l i c a b l e "  
 p r o m p t _ b o o   " I s   I D G   f i l t e r   O K ? " ,   C S D F i l O K  
 I f   C S D F i l O K   =   T R U E   T h e n  
 r e s u l t   " I D G   f i l t e r   i s   O K " ,   R E P O R T   &   " O i l F i l t e r C h k "  
 E l s e  
 r e s u l t   " I D G   f i l t e r   i s   n o t   O K " ,   R E P O R T   &   " O i l F i l t e r C h k "  
 E n d   I f  
  
 ' *     V 1 . 0 2   i n s t r u c t i o n   " R e - E n g a g e   I D G . "  
 i n s t r u c t i o n   " R e - E n g a g e   I D G   i f   a p p l i c a b l e . "  
 p r o m p t _ b o o   " D i d   y o u   R e - E n g a n g e   I D G ? . " ,   I D G R e E n g  
 I f   I D G R e E n g   =   T R U E   T h e n  
 r e s u l t   " T h e   I D G   w a s   R e - E n g a g e d . " ,   R E P O R T   &   " S h u t d o w n _ C h e c k "  
 E l s e  
 r e s u l t   " T h e   I D G   w a s   n o t   R e - E n g a g e d . " ,   R E P O R T   &   " S h u t d o w n _ C h e c k "  
 E n d   I f  
 ' *     V 1 . 0 2   a d d e d   e n d i f  
 E n d   I f  
  
 i n s t r u c t i o n   "   C h e c k   a l l   o i l   l e v e l s "  
 p r o m p t _ b o o   " W e r e   o i l   l e v e l s   c h e c k e d   a n d   t o p p e d   u p   a s   r e q u i r e d ? " ,   O i l L e v e l O K  
 I f   O i l L e v e l O K   =   T R U E   T h e n  
 r e s u l t   " O i l   l e v e l s   w e r e   c h e c k e d   a n d   r e t o p p e d " ,   R E P O R T   &   " O i l L e v e l C h e c k "  
 E l s e  
 r e s u l t   " O i l   l e v e l s   a r e   n o t   s a t i s f a c t o r y " ,   R E P O R T   &   " O i l L e v e l C h e c k "  
 E n d   I f  
  
 i n s t r u c t i o n   " C h e c k   i n t a k e   a n d   e x h a u s t . "  
 p r o m p t _ b o o   " W a s   i n t a k e   a n d   e x h a u s t   c h e c k   s a t i s f a c t o r y ? " ,   I n _ E x h O K  
 I f   I n _ E x h O K   =   T R U E   T h e n  
 r e s u l t   " I n t a k e   a n d   e x h a u s t   c h e c k e d   O K . " ,   R E P O R T   &   " I n t a k e E x h a u s t C h e c k "  
 E l s e  
 r e s u l t   " A   p r o b l e m   w a s   f o u n d   i n   t h e   i n t a k e   o r   e x h a u s t . " ,   R E P O R T   &   " I n t a k e E x h a u s t C h e c k "  
 E n d   I f  
  
 i n s t r u c t i o n   " C h e c k   r o t o r s   f o r   f r e e d o m   o f   r o t a t i o n . "  
 p r o m p t _ b o o   " W e r e   r o t o r s   r o t a t i o n   f o u n d   s a t i s f a c t o r y   w h e n   c h e c k e d ? " ,   R o t o r R o t  
 I f   R o t o r R o t   =   T R U E   T h e n  
 r e s u l t   " R o t o r s   r o t a t i o n   f o u n d   s a t i s f a c t o r y . " ,   R E P O R T   &   " R o t o r R o t a t i o n "  
 E l s e  
 r e s u l t   " R o t o r s   r o t a t i o n   w e r e   n o t   s a t i s f a c t o r y " ,   R E P O R T   &   " R o t o r R o t a t i o n "  
 E n d   I f  
  
 i n s t r u c t i o n   " R e m o v e   a l l   t e s t   e q u i p m e n t "  
 p r o m p t _ b o o   " I s   t e s t   e q u i p m e n t   r e m o v e d ? " ,   T e s t E q R e m  
 I f   T e s t E q R e m   =   T R U E   T h e n  
 r e s u l t   " T e s t   e q u i p m e n t   i s   r e m o v e d " ,   R E P O R T   &   " T e s t E q u i p m e n t "  
 E l s e  
 r e s u l t   " T e s t   e q u i p m e n t   i s   n o t   r e m o v e d " ,   R E P O R T   &   " T e s t E q u i p m e n t "  
 E n d   I f  
  
 d o _ f u l l s e t   1 ,   " T e s t   f i n i s h " ,   " T e s t C o n c l u s i o n "  
 