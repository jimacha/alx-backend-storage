Curriculum <br>
**Short Specializations** <br>

# 0x02. Redis basic

# Redis Basics README

## Introduction to Redis

Redis is an open-source, advanced key-value store. It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets, and sorted sets. Redis is commonly used as a backend data store, caching mechanism, and message broker. It's designed for high performance, scalability, and simplicity.

## Key Features

- **In-Memory Data Store:** Redis stores all its data in RAM, allowing for extremely fast read and write operations.

- **Data Structures:** Redis supports various data types, including strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, and geospatial indexes.

- **Persistence:** Redis can persist data to disk, allowing you to save your data even after restarting the server.

- **Replication:** Redis supports master-slave replication, enabling data redundancy and high availability.

- **Partitioning:** Redis allows you to split your data across multiple Redis instances, improving scalability.

- **Pub/Sub Messaging:** Redis supports publish/subscribe messaging patterns, making it an excellent choice for building real-time applications.

## Basic Redis Commands

### Strings

- `SET key value`: Set the value of a key.
- `GET key`: Get the value of a key.
- `DEL key`: Delete a key.

### Lists

- `LPUSH key value`: Insert a value at the beginning of a list.
- `RPUSH key value`: Insert a value at the end of a list.
- `LRANGE key start stop`: Get a range of elements from a list.

### Sets

- `SADD key member`: Add a member to a set.
- `SMEMBERS key`: Get all the members of a set.
- `SISMEMBER key member`: Check if a member exists in a set.

### Hashes

- `HSET key field value`: Set the value of a hash field.
- `HGET key field`: Get the value of a hash field.
- `HGETALL key`: Get all fields and values from a hash.

### Sorted Sets

- `ZADD key score member`: Add a member to a sorted set with a score.
- `ZRANGE key start stop`: Get a range of elements from a sorted set.

### Additional Commands

- `PING`: Check if the server is running.
- `INFO`: Get information and statistics about the server.
- `FLUSHALL`: Remove all keys from all databases.

## Using Redis as a Backend

Redis can be used as a backend data store in various applications, including web applications, mobile apps, and IoT devices. Its speed and flexibility make it an ideal choice for scenarios where quick access to data is essential.

### Setting Up Redis as a Backend

1. **Installation:** Install Redis on your server or local machine. You can download it from the official [Redis website](https://redis.io/download).

2. **Configuration:** Configure the `redis.conf` file to customize Redis settings according to your requirements.

3. **Connecting to Redis:** Use Redis clients in your preferred programming language to connect to the Redis server and perform read and write operations.

Example (Python):

```python
import redis

# Connect to Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Set a key
redis_client.set('example_key', 'example_value')

# Get the value of a key
value = redis_client.get('example_key')
print(value.decode('utf-8'))  # Output: 'example_value'
```

## Conclusion

Redis is a powerful and versatile data store that can be utilized as a backend solution for various applications. Its rich set of data structures, speed, and ease of use make it a popular choice among developers. By mastering the basics of Redis, you can enhance the performance and scalability of your applications.