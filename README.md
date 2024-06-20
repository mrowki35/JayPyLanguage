# Dokumentacja Języka Programowania Japy

## Spis treści
1. [Wprowadzenie](#wprowadzenie)
2. [Typy danych](#typy-danych)
3. [Zmienne](#zmienne)
4. [Podstawowe operacje](#podstawowe-operacje)
    - [Operacje arytmetyczne](#operacje-arytmetyczne)
    - [Operacje logiczne](#operacje-logiczne)
5. [Instrukcje sterujące](#instrukcje-sterujące)
    - [If-Else](#if-else)
    - [Pętla For](#pętla-for)
    - [Pętla For-In](#pętla-for-in)
    - [While](#while)
6. [Operacje na macierzach](#operacje-na-macierzach)
7. [Funkcje](#funkcje)
    - [Deklaracja funkcji](#deklaracja-funkcji)
    - [Wywołanie funkcji](#wywolanie-funkcji)
8. [Użycie języka](#uzycie-jezyka)

## Wprowadzenie
Japy to język programowania łączący składnię Javy z niektórymi funkcjonalnościami Pythona, co czyni go wygodnym do użytku w różnych zastosowaniach.

## Typy danych
Japy obsługuje różne typy danych, podobnie jak Java:

### Typy proste
- `int` - liczby całkowite 
- `float` - liczby zmiennoprzecinkowe pojedynczej precyzji
- `double` - liczby zmiennoprzecinkowe podwójnej precyzji
- `boolean` - wartości logiczne (`true`/`false`)

### Typy złożone
- `String` - ciągi znaków
- `Array` - tablice
- `Array[Array]` - macierze

## Zmienne
Zmienne w Japy deklaruje się podobnie jak w Javie:

```java
int liczba = 10;
float liczbaZmiennoprzecinkowa = 10.5;
boolean prawda = true;
String tekst = "Hello, Japy!";
```

## Podstawowe operacje
### Operacje arytmetyczne
Operacje arytmetyczne w Japy są takie same jak w Javie:

- Dodawanie (`+`)
- Odejmowanie (`-`)
- Mnożenie (`*`)
- Dzielenie (`/`)
= Reszta z dzielenia (`%`)

```java
int a = 10;
int b = 5;

int suma = a + b;       // 15
int roznica = a - b;    // 5
int iloczyn = a * b;    // 50
int iloraz = a / b;     // 2
int reszta = a % b;     // 0
```

Operacje na liczbach zmiennoprzecinkowych działają podobnie:
```java
double x = 10.0;
double y = 3.0;

double suma = x + y;       // 13.0
double roznica = x - y;    // 7.0
double iloczyn = x * y;    // 30.0
double iloraz = x / y;     // 3.333...
double reszta = x % y;     // 1.0
```

### Operacje logiczne
Operacje logiczne w Japy również są takie same jak w Javie:

- AND (`&&`)
- OR (`||`)
- NOT (`!`)

```java
boolean prawda = true;
boolean falsz = false;

boolean andWynik = prawda && falsz;   // false
boolean orWynik = prawda || falsz;    // true
boolean notWynik = !prawda;           // false
```

Operacje porównania:

- Równość (`==`)
- Nierówność (`!=`)
- Większe (`>`)
- Mniejsze (`<`)
- Większe lub równe (`>=`)
- Mniejsze lub równe (`<=`)

```java
int a = 10;
int b = 5;

boolean rowne = (a == b);           // false
boolean nierowne = (a != b);        // true
boolean wieksze = (a > b);          // true
boolean mniejsze = (a < b);         // false
boolean wiekszeLubRowne = (a >= b); // true
boolean mniejszeLubRowne = (a <= b);// false
```

## Instrukcje sterujące
### If-Else
Instrukcje warunkowe działają podobnie jak w Javie:

```java
int a = 10;
if (a > 5) {
    println("a jest większe od 5");
} else {
    println("a jest mniejsze lub równe 5");
}
```

### Pętla For
Pętla for działa jak w Javie:

```java
for (int i = 0; i < 10; i++) {
    println(i);
}
```

### Pętla For-In
Pętla for-in działa jak w Pythonie:

```python
int[] tablica = {1, 2, 3, 4, 5};
for (int element in tablica) {
    println(element);
}
```

### While
Pętla while działa jak w Javie:

```java
int i = 0;
while (i < 5) {
    println(i);
    i++;
}
```

## Operacje na macierzach
Japy obsługuje operacje na macierzach zbliżone do tych w Pythonie, co ułatwia pracę z danymi numerycznymi:

### Tworzenie macierzy
```java
float[] macierz = {{1, 2}, {3, 4}}; // Tworzy macierz 2x2
```

### Operacje arytmetyczne
```java
float[] macierz1 = {{1, 2}, {3, 4}};
float[] macierz2 = {{5, 6}, {7, 8}};

float[] suma = macierz1 + macierz2; // Dodawanie macierzy
float[] roznica = macierz1 - macierz2; // Odejmowanie macierzy
float[] iloczynElementow = macierz1 * macierz2; // Mnożenie element przez element
float[] dzielenie = macierz1 / macierz2; // Dzielenie macierzy
float[] iloczyn = macierz1 DOT macierz2; // Mnożenie macierzy
```

## Funkcje
### Deklaracja funkcji
Deklarowanie funkcji w Japy jest podobne do deklarowania metod w Javie:

```java
// Funkcja bez argumentów i bez wartości zwracanej
void wypiszPowitanie() {
    System.out.println("Witaj, Japy!");
}

// Funkcja z argumentami i bez wartości zwracanej
void wypiszLiczbe(int liczba) {
    System.out.println("Liczba: " + liczba);
}

// Funkcja z argumentami i wartością zwracaną
int dodaj(int a, int b) {
    return a + b;
}
```

### Wywołanie funkcji
Wywołanie funkcji w Japy jest takie samo jak w Javie:

```java
wypiszPowitanie(); // Wywołanie funkcji bez argumentów

wypiszLiczbe(10); // Wywołanie funkcji z argumentem

int wynik = dodaj(5, 7); // Wywołanie funkcji z argumentami i przypisanie wartości zwracanej do zmiennej
println("Wynik: " + wynik); // Wypisanie wyniku
```


## Użycie języka
Użycie języka polega na napisaniu kodu w input string pomiędzy `""" """`.

```java
"""
int main() {
  return 1;
}
"""
```
