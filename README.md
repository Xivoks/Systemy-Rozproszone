# Systemy-Rozproszone

### Instrukcja instalacji i uruchomienia

Zainstaluj Python 3.8.x na swoim systemie operacyjnym. Możesz to zrobić, na przykład, korzystając z menedżera pakietów systemowych, np. apt-get na Ubuntu:
```
sudo apt-get update
sudo apt-get install python3.8
```
Upewnij się, że Python został pomyślnie zainstalowany, wykonując komendę:
```
python3.8 --version
```
Zainstaluj PyRPC, wykonując komendę:
```
pip install PyRPC
```
Możesz sprawdzić, czy PyRPC zostało pomyślnie zainstalowane, wykonując:
```
python3.8 -c "import pyRpc; print(pyRpc.__version__)"
```
Uruchom serwer, wykonując komendę:
```
python3.8 server.py
```
Uruchom klienta, wykonując komendę:
```
python3.8 client.py
```
