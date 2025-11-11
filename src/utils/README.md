# cache-redis-config

A library for managing Redis cache configurations with ease.

## Overview

`cache-redis-config` simplifies the process of defining, loading, and applying Redis cache configurations in your applications. It provides a flexible and type-safe way to manage connection details, key prefixes, expiration policies, and other cache-related settings.

## Features

*   **Configuration Loading:** Load configurations from various sources, including environment variables, JSON files, and YAML files.
*   **Type Safety:** Define cache configurations using TypeScript interfaces for improved code maintainability.
*   **Connection Management:** Easily configure Redis connection details, such as host, port, password, and database.
*   **Key Prefixes:** Automatically apply key prefixes to avoid naming conflicts in shared Redis instances.
*   **Expiration Policies:** Set default expiration times for cached data.
*   **Customizable Serialization:** Support for custom serialization/deserialization of cached values.
*   **Easy Integration:** Simple API for integrating with popular caching libraries.

## Installation

```bash
npm install cache-redis-config
# or
yarn add cache-redis-config
# or
pnpm add cache-redis-config
```

## Usage

```typescript
import { RedisConfigLoader } from 'cache-redis-config';

// Example configuration interface
interface MyCacheConfig {
    host: string;
    port: number;
    keyPrefix: string;
}

// Load configuration from environment variables
const config = RedisConfigLoader.loadFromEnv<MyCacheConfig>({
    host: 'REDIS_HOST',
    port: 'REDIS_PORT',
    keyPrefix: 'MY_CACHE_PREFIX',
});

// Alternatively, load from a JSON file
// const config = RedisConfigLoader.loadFromJson<MyCacheConfig>('./config.json');

// Now you can use the config to connect to Redis
import Redis from 'ioredis';

const redis = new Redis({
    host: config.host,
    port: config.port,
});

// Example usage with key prefix
const key = config.keyPrefix + ':myKey';

async function example() {
    await redis.set(key, 'myValue');
    const value = await redis.get(key);
    console.log(value); // Output: myValue
}

example();
```

## Configuration Options

The configuration options can be specified via environment variables, JSON, or YAML files.

| Option      | Environment Variable | JSON Key    | YAML Key   | Description                                        |
| ----------- | -------------------- | ----------- | ---------- | -------------------------------------------------- |
| host        | REDIS_HOST           | host        | host       | Redis host.                                        |
| port        | REDIS_PORT           | port        | port       | Redis port.                                        |
| password    | REDIS_PASSWORD       | password    | password   | Redis password.                                    |
| db          | REDIS_DB             | db          | db         | Redis database.                                    |
| keyPrefix   | REDIS_KEY_PREFIX     | keyPrefix   | keyPrefix  | Key prefix for all cache keys.                     |
| ttl         | REDIS_TTL            | ttl         | ttl        | Default time-to-live (in seconds) for cache entries.|
| tls         | REDIS_TLS            | tls         | tls        | Enable TLS connection to Redis (boolean or object). |
| username    | REDIS_USERNAME       | username    | username   | Redis username.                                    |

## Contributing

Contributions are welcome! Please submit pull requests with clear descriptions of the changes.

## License

MIT