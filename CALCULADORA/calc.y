%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double derivada(double (*func)(double), double x, double h);
double calcular_integral(double a, double b, double (*func)(double), int n);
double log_base(double base, double x);

void yyerror(const char *s);
int yylex(void);
%}

// tokens
%union {
    double num;                      // Para números
    double (*func_ptr)(double);      // Para funciones
}

%token <num> NUMBER
%token <func_ptr> SIN COS EXP LOG SQRT TAN ATAN SINH
%token EOL LOG_BASE
%token DERIVADA INTEGRAL
%type <num> exp
%type <func_ptr> func

%left '+' '-'
%left '*' '/'
%nonassoc UMINUS

// Reglas de gramática
%%
input:
    | input line
    ;

line:
    exp EOL { printf("%g\n", $1); }
    ;

exp:
      NUMBER { $$ = $1; }
    | exp '+' exp { $$ = $1 + $3; }
    | exp '-' exp { $$ = $1 - $3; }
    | exp '*' exp { $$ = $1 * $3; }
    | exp '/' exp { 
        if ($3 == 0) {
            yyerror("Division por cero");
            YYABORT;
        }
        $$ = $1 / $3; 
      }
    | '-' exp %prec UMINUS { $$ = -$2; }
    | '(' exp ')' { $$ = $2; }
    | func '(' exp ')' { $$ = $1($3); }
    | DERIVADA '(' func ',' exp ')' { $$ = derivada($3, $5, 1e-5); }
    | INTEGRAL '(' exp ',' exp ',' func ',' exp ')' { $$ = calcular_integral($3, $5, $7, (int)$9); }
    | LOG_BASE '(' exp ',' exp ')' { 
        if ($5 <= 0 || $3 <= 0) {
            yyerror("Base o argumento inválido para logaritmo");
            YYABORT;
        }
        $$ = log_base($3, $5); 
      }
    ;

func:
      SIN { $$ = sin; }
    | COS { $$ = cos; }
    | EXP { $$ = exp; }
    | LOG { $$ = log; }
    | SQRT { $$ = sqrt; }
    | TAN { $$ = tan; }
    | ATAN { $$ = atan; }
    | SINH { $$ = sinh; }
    ;

%%

// Implementación de las funciones
double derivada(double (*func)(double), double x, double h) {
    return (func(x + h) - func(x - h)) / (2 * h);
}

double calcular_integral(double a, double b, double (*func)(double), int n) {
    if (n <= 0) {
        fprintf(stderr, "Error: el número de intervalos debe ser mayor que cero.\n");
        exit(EXIT_FAILURE);
    }
    double h = (b - a) / n;
    double integral = 0.0;

    for (int i = 0; i < n; i++) {
        double x1 = a + i * h;
        double x2 = x1 + h;
        integral += (func(x1) + func(x2)) / 2 * h; 
    }

    return integral;
}

double log_base(double base, double x) {
    return log(x) / log(base);
}

int main() {
    
    return yyparse();
}

void yyerror(const char *s) {
   
    fprintf(stderr, "Error en el cálculo: %s\n", s);
}
