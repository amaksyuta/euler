export const environment = {
    development: true,
    test: false,
    production: false,

    // Development version
    version: 0.71,

    getCurrentEnvironment: () => 'development',

    restApi: {
        // apiBaseUrl: 'https://<SERVER_NAME>.mxvirtual.com/',

        // Max number of attepts for which failed API should be retried
        // Note: Actual API sent = Initial API call which was failed + maxRetryAttempts
        maxRetryAttempts: 0,
        retryDelay: 200,
    },

    webSocket: {
        // webSocketUrl: 'wss://<SERVER_NAME>.mxvirtual.com:7779',
    },
};
