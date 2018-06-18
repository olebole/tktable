%{
%}

#include coordsys.tin
#include wcssys.tin

%start framesend

%token ACTIVE_
%token ALL_
%token AUX_
%token BIN_
%token CONTOUR_
%token CUBE_
%token DATAMIN_
%token DATASEC_
%token EQUATORIAL_
%token FITS_
%token FRAMENO_
%token GRID_
%token HAS_
%token HIGHLITE_
%token IIS_
%token IRAFMIN_
%token LINEAR_
%token LOCK_
%token MARKER_
%token MOSAIC_
%token PASTE_
%token SELECT_
%token SMOOTH_
%token SYSTEM_
%token UNDO_

%%

#include coordsys.trl
#include wcssys.trl

framesend : {FrameSendCmd}
 | FRAMENO_ {FrameSendCmd}
 | LOCK_ {ProcessSendCmdGet panzoom lock}
 | ACTIVE_ {FrameSendCmdGet active}
 | ALL_ {FrameSendCmdGet frames}
 | HAS_ has
 ;

has : coordsys {ProcessSendCmdCurrentYesNo frame "has $1"}
 | wcssys {ProcessSendCmdCurrentYesNo frame "has wcs $1"}
 | param {ProcessSendCmdCurrentYesNo frame "has $1"}
 | CONTOUR_ contour {ProcessSendCmdCurrentYesNo frame "has contour $2"}
 | FITS_ fits {ProcessSendCmdCurrentYesNo frame "has fits $2"}
 | MARKER_ marker  {ProcessSendCmdCurrentYesNo frame "has marker $2"}
 | SYSTEM_ system
 | WCS_ wcs
 ; 

param : IIS_ {set _ iis}
 | DATAMIN_ {set _ datamin}
 | IRAFMIN_ {set _ irafmin}
 | DATASEC_ {set _ datasec}
 | GRID_ {set _ grid}
 | SMOOTH_ {set _ smooth}
 ;

contour : {set _ {}}
 | AUX_ {set _ aux}
 ;

fits : {set _ {}}
 | BIN_ {set _ bin}
 | CUBE_ {set _ cube}
 | MOSAIC_ {set _ mosaic}
 ;

marker : HIGHLITE_ {set _ highlite}
 | PASTE_ {set _ paste}
 | SELECT_ {set _ select}
 | UNDO_ {set _ undo}
 ;

system : coordsys {ProcessSendCmdCurrentYesNo frame "has $1"}
 | wcssys {ProcessSendCmdCurrentYesNo frame "has wcs $1"}
 ;
 
wcs : wcssys {ProcessSendCmdCurrentYesNo frame "has wcs $1"}
 | wcstype wcssys {ProcessSendCmdCurrentYesNo frame "has wcs $1 $2"}
 ;

wcstype : EQUATORIAL_ {set _ equatorial}
 | LINEAR_ {set _ linear}
 ;

%%

proc framesend::yyerror {msg} {
     variable yycnt
     variable yy_current_buffer
     variable index_

     ParserError $msg $yycnt $yy_current_buffer $index_
}
