CREATE TABLE flights (
id INT PRIMARY KEY,
datetime DATE,
airport_code TEXT,
city TEXT,
flight_number INT,	 	
departure_delay decimal,
cancellation INT
);

CREATE TABLE weather (
id INT PRIMARY KEY,
datetime DATE,
atlanta TEXT,
chicago TEXT,
kansas_city TEXT,
new_york TEXT,
san_francisco TEXT
);