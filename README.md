# cache-redis-config

A comprehensive cache configuration library for Redis.

## Description

cache-redis-config is a lightweight, easy-to-use library that allows you to configure and manage Redis cache settings in your application. It provides a simple and intuitive API for setting up and customizing Redis connections, expiration policies, and other cache-related settings.

## Features

*   **Flexible configuration**: cache-redis-config allows you to configure Redis connections, expiration policies, and other cache-related settings using a simple and intuitive API.
*   **Support for multiple Redis connections**: Easily manage multiple Redis connections with cache-redis-config, perfect for large-scale applications with multiple Redis instances.
*   **Automatic connection pooling**: cache-redis-config provides automatic connection pooling, ensuring efficient and scalable Redis connections.
*   **Configurable expiration policies**: Set custom expiration policies for your cache, including time-to-live (TTL) and eviction policies.
*   **High-performance**: cache-redis-config is designed for high-performance applications, ensuring fast and efficient Redis interactions.

## Technologies Used

*   **Node.js**: cache-redis-config is built on top of Node.js, ensuring seamless integration with popular Node.js frameworks and libraries.
*   **Redis**: cache-redis-config is designed to work with Redis, providing a simple and efficient way to interact with Redis cache.
*   **TypeScript**: cache-redis-config is written in TypeScript, ensuring robust and maintainable code.

## Installation

### Prerequisites

*   **Node.js**: cache-redis-config requires Node.js 14.17.0 or later.
*   **Redis**: cache-redis-config requires a Redis server to be installed and running.

### Installation Steps

1.  **Install cache-redis-config**: Run `npm install cache-redis-config` or `yarn add cache-redis-config` to install the library.
2.  **Import cache-redis-config**: Import the library in your application using `const CacheRedisConfig = require('cache-redis-config');` or `import CacheRedisConfig from 'cache-redis-config';`.
3.  **Configure Redis connections**: Configure Redis connections using the `CacheRedisConfig` API.

## Example Usage

```typescript
import CacheRedisConfig from 'cache-redis-config';

const config = new CacheRedisConfig({
    host: 'localhost',
    port: 6379,
    db: 0,
    password: 'your_password',
    options: {
        maxConnections: 10,
        maxIdle: 5,
    },
});

// Set cache expiration policy
config.setExpirationPolicy({
    ttl: 3600, // 1 hour
    evictionPolicy: 'LRU',
});

// Get Redis client instance
const redisClient = config.getRedisClient();

// Use Redis client instance
redisClient.set('my_key', 'my_value', (err, reply) => {
    if (err) {
        console.error(err);
    } else {
        console.log(reply);
    }
});
```

## Contributing

We welcome contributions to cache-redis-config! Please see our [Contributing Guide](CONTRIBUTING.md) for more information on how to contribute to the project.

## License

cache-redis-config is released under the [MIT License](LICENSE.md).