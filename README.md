# Systemy Rozproszone

## Kalkulator RPC

Projekt ten jest prostym przykładem implementacji kalkulatora wykorzystującego zdalne wywołania procedur (RPC) za pomocą biblioteki PyRPC. Kalkulator umożliwia wykonywanie podstawowych operacji matematycznych, takich jak dodawanie, odejmowanie, mnożenie i dzielenie, na serwerze.

## Instrukcje instalacji

1. Zainstaluj Python 3.8.x na swoim systemie operacyjnym. Możesz to zrobić, na przykład, używając menedżera pakietów systemowych, takiego jak `apt-get` na Ubuntu. Oto przykładowe komendy dla Ubuntu:

```
sudo apt-get update
sudo apt-get install python3.8
```

2. Upewnij się, że Python został pomyślnie zainstalowany, wykonując komendę:

```
python3.8 --version
```

3. Zainstaluj bibliotekę PyRPC, wykonując komendę:

```
pip install PyRPC
```

4. Możesz sprawdzić, czy PyRPC zostało pomyślnie zainstalowane, wykonując:

```
python3.8 -c "import pyRpc; print(pyRpc.version)"
```

## Uruchamianie serwera

Aby uruchomić serwer, wykonaj następujące kroki:

1. Otwórz terminal i przejdź do katalogu, w którym znajduje się plik `server.py`.

2. Uruchom serwer, wykonując komendę:

```
python3.8 server.py
```
3. Serwer zostanie uruchomiony i będzie nasłuchiwał na żądania klienta.

## Uruchamianie klienta

Aby uruchomić klienta i korzystać z funkcji kalkulatora, wykonaj następujące kroki:

1. Otwórz nowy terminal i przejdź do katalogu, w którym znajduje się plik `client.py`.

2. Uruchom klienta, wykonując komendę:
  
```
python3.8 client.py
```

3. Klient nawiąże połączenie z serwerem i wyśle żądania dotyczące operacji matematycznych.

4. Wyniki operacji zostaną wyświetlone na konsoli.

## Dostępne operacje

Kalkulator umożliwia wykonanie następujących operacji matematycznych:

- Dodawanie: `remote.call("add", args=(a, b), callback=response)`
- Odejmowanie: `remote.call("subtract", args=(a, b), callback=response)`
- Mnożenie: `remote.call("multiply", args=(a, b), callback=response)`
- Dzielenie: `remote.call("divide", args=(a, b), callback=response)`

Gdzie `a` i `b` są liczbami, które chcesz poddać danej operacji. Wynik zostanie wyświetlony na konsoli.

## Zamykanie serwera

Po zakończeniu korzystania z kalkulatora, można zamknąć serwer, wykonując kombinację klawiszy `Ctrl + C` w terminalu, w którym uruchomiono serwer.

```
myRpc.stop()
```

## Zawartość projektu

- `client.py`: Moduł klienta, który nawiązuje połączenie z serwerem i wysyła żądania dotyczące operacji matematycznych.
- `server.py`: Moduł serwera, który nasłuchuje na żądania klienta i wykonuje operacje matematyczne.
- `pyRpc`: Biblioteka PyRPC, wymagana do komunikacji między klientem a serwerem.

```
Projekt:
├── client.py
├── server.py
└── pyRpc/
```

Życzę udanego korzystania z kalkulatora RPC!
