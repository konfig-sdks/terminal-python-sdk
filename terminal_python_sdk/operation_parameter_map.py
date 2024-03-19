operation_parameter_map = {
    '/public-token/exchange-POST': {
        'parameters': [
            {
                'name': 'publicToken'
            },
        ]
    },
    '/connections-POST': {
        'parameters': [
            {
                'name': 'tags'
            },
            {
                'name': 'backfill'
            },
            {
                'name': 'company'
            },
            {
                'name': 'credentials'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'syncMode'
            },
        ]
    },
    '/connections/current-GET': {
        'parameters': [
            {
                'name': 'connection-token'
            },
        ]
    },
    '/connections-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'dotNumber'
            },
            {
                'name': 'tag'
            },
        ]
    },
    '/connections/current-PATCH': {
        'parameters': [
            {
                'name': 'tags'
            },
            {
                'name': 'company'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'syncMode'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/syncs/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/syncs-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'status'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/passthrough-POST': {
        'parameters': [
            {
                'name': 'body'
            },
            {
                'name': 'headers'
            },
            {
                'name': 'method'
            },
            {
                'name': 'path'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/syncs-POST': {
        'parameters': [
            {
                'name': 'days'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/devices-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/drivers/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/drivers-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/groups-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/hos/available-time-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'driverIds'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/hos/daily-logs-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'driverIds'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/hos/logs-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'startedAfter'
            },
            {
                'name': 'startedBefore'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'driverIds'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/ifta/summary-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'startMonth'
            },
            {
                'name': 'endMonth'
            },
            {
                'name': 'groupBy'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/issues-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'lastReportedAfter'
            },
            {
                'name': 'lastReportedBefore'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connectionId'
            },
            {
                'name': 'errorCode'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/issues/{issueId}/resolve-POST': {
        'parameters': [
            {
                'name': 'issueId'
            },
        ]
    },
    '/providers-GET': {
        'parameters': [
        ]
    },
    '/safety/events-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'startedAfter'
            },
            {
                'name': 'startedBefore'
            },
            {
                'name': 'driverIds'
            },
            {
                'name': 'vehicleIds'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/trailers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/trailers/locations-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/trips-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'startedAfter'
            },
            {
                'name': 'startedBefore'
            },
            {
                'name': 'endedAfter'
            },
            {
                'name': 'endedBefore'
            },
            {
                'name': 'driverIds'
            },
            {
                'name': 'vehicleIds'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/vehicles-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'modifiedAfter'
            },
            {
                'name': 'modifiedBefore'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/vehicles/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/vehicles/{vehicleId}/stats/historical-GET': {
        'parameters': [
            {
                'name': 'vehicleId'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'endAt'
            },
            {
                'name': 'types'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/vehicles/locations-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'vehicleIds'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
    '/vehicles/{vehicleId}/locations-GET': {
        'parameters': [
            {
                'name': 'vehicleId'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'endAt'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'connection-token'
            },
        ]
    },
};