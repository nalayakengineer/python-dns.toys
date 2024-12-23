# DNS Server in Python ☁️

This project implements a simple DNS server in Python that can respond with TXT queries. 

This project was inspired by [Kailash Nadh's](https://github.com/knadh) dns.toys. dns.toys is a similar DNS server written in Go has a huge community support. 

--> https://github.com/knadh/dns.toys

For Learning, I've tried to recreate the same in python. I'll be working on adding more utilities with time. ☺️



## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dns-server.git
   cd dns-server
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the DNS server, run the following command:
```
python src/server.py

```

The server will listen for incoming DNS queries on your local address and respond with TXT record.

## How It Works

- The `server.py` file sets up the DNS server and handles incoming requests.
- The helper function handlers are inside the utils directory. 
- 

## Currently available helpers
- Get Time for a specific city: 

```
dig mumbai.time @0.0.0.0
dig london.time @0.0.0.0
```

- Get epoch time or convert epoch time to Human readable Date-time

```
dig now.epoch @0.0.0.0
dig 183792.epoch@0.0.0.0
```

- Get random number between a range.
```
dig 1-100.random @0.0.0.0
dig 1002-19992.random @0.0.0.0
```

- Do base conversions 
```
dig 101-dec-bin.base @0.0.0.0
dig 121-hex-oct.base @0.0.0.0
```


## Contributing

Feel free to submit issues or pull requests.

