%{
#include <stdio.h>
#include <stdlib.h>
#include "calc.tab.h"  
%}

%%

[0-9]+(\.[0-9]+)?  { yylval.num = atof(yytext); return NUMBER; }
\n                  { return EOL; }
"log_base"          { return LOG_BASE; }
"sin"               { return SIN; }
"cos"               { return COS; }
"exp"               { return EXP; }
"log"               { return LOG; }
"sqrt"              { return SQRT; }
"tan"               { return TAN; }
"atan"              { return ATAN; }
"sinh"              { return SINH; }
"derivada"          { return DERIVADA; }
"integral"          { return INTEGRAL; }
[ \t]+              { /* Ignorar espacios y tabs */ }
.                   { return yytext[0]; } 

%%

int yywrap() {
    return 1;
}
