export const environment = {
    development: false,
    test: true,
    production: false,

    // Test version
    version: 0.70,

    getCurrentEnvironment: () => 'test',

    restApi: {
        // apiBaseUrl: 'https://<SERVER_NAME>.mxvirtual.com/',

        // Max number of attepts for which failed API should be retried
        // Note: Actual API sent = Initial API call which was failed + maxRetryAttempts
        maxRetryAttempts: 0,
        retryDelay: 200,
    },

    webSocket: {
        // webSocketUrl: 'wss://<SERVER_NAME>.mxvirtual.com:7779'
    },
};
