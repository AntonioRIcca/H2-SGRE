par = dict()

par['EL101'] = {
    'Pset': 0,
    'Pread': 0,
    'H2': 2.6,
    'start': False,
    'log': '',
    'status': 'on',
    'pressure': 0,
    'mb': {
        'w': {
            'commands': {
                'val': 0,
                'reg': 49852
            },
            'ResetLifeDeionizer': {
                'val': 0,
                'reg': 49869
            },
            'Default': {
                'val': 0,
                'reg': 49166
            }
        },
        'r': {
            'MS': {
                'val': 0,
                'reg': 53258
            },
            'LS': {
                'val': 0,
                'reg': 53258
            },
            'FlowLimit': {
                'val': 0,
                'reg': 49854
            },
            'IntPressure': {
                'val': 0,
                'reg': 49855
            },
            'OutPressure': {
                'val': 0,
                'reg': 49856
            },
            'Flow': {
                'val': 0,
                'reg': 49857
            },
            'Production': {
                'val': 0,
                'reg': [49858, 49859]
            },
            'CellPower': {
                'val': 0,
                'reg': 49860
            },
            'CellCurrent': {
                'val': 0,
                'reg': 50063
            },
            'CellVoltage': {
                'val': 0,
                'reg': 50062
            },
            'PSTemperature': {
                'val': 0,
                'reg': 49861
            },
            'VoltAlim': {
                'val': 0,
                'reg': 49862
            },
            'WaterLevel': {
                'val': 0,
                'reg': 49863
            },
            'WaterQuality%': {
                'val': 0,
                'reg': 49864
            },
            'WaterQualityuS': {
                'val': 0,
                'reg': 50053
            },
            'Alarm': {
                'val': 0,
                'reg': 49865
            },
            'PreAlarm': {
                'val': 0,
                'reg': [49866, 49867]
            },
            'LifeATime': {
                'val': 0,
                'reg': [49560, 49561]
            },
            'DeionizerLife': {
                'val': 0,
                'reg': [49562, 49563]
            },
            'DryerLife': {
                'val': 0,
                'reg': [49564, 49565]
            },
            'LifeTime': {
                'val': 0,
                'reg': 53389
            },
            'H2Produced': {
                'val': 0,
                'reg': 53390
            },
            'DeionizerLifeCountdown': {
                'val': 0,
                'reg': 53394
            },
            'DrierLifeCountdown': {
                'val': 0,
                'reg': 53395
            },
            'DryerStatus': {
                'val': 0,
                'reg': 53396
            },
            'SignalIr1': {
                'val': 0,
                'reg': 50079
            },
            'SignalIr2': {
                'val': 0,
                'reg': 50080

            }
        },
        'rw': {
            'OutPressSet': {
                'val': 0,
                'reg': 49853
            },
            'StatoRefill': {
                'val': 0,
                'reg': 49868
            },
            'BlockMachine': {
                'val': 0,
                'reg': 49574
            },
            'PressDropDelay': {
                'val': 120,
                'reg': 49152
            },
            'OutPressMinRIse': {
                'val': 200,
                'reg': 49153
            },
            'AutoStart': {
                'val': 1,
                'reg': 49154
            },
            'PressureUnits': {
                'val': 0,
                'reg': 49155
            },
            'TempUnits': {
                'val': 0,
                'reg': 49156
            },
            'CanisterCapacity': {
                'val': 5,
                'reg': 49157
            },
            'AutoRefillMode': {
                'val': 0,
                'reg': 49158
            },
            'StartMode': {
                'val': 0,
                'reg': 49159
            },
            'IDAddress': {
                'val': 1,
                'reg': 49160
            },
            'BaudRateRS845': {
                'val': 3,
                'reg': 49161
            },
            'ZeroAir': {
                'val': 0,
                'reg': 49162
            },
            'Hydrogenation': {
                'val': 0,
                'reg': 49163
            },
            'H2Sensor': {
                'val': 0,
                'reg': 49164
            },
            'UserFlowLimit': {
                'val': 100,
                'reg': 49165
            },
            'AutomaticIntCheck': {
                'val': 1,
                'reg': 49167
            },
            'RemoteContactMode': {
                'val': 0,
                'reg': 49168
            },
            'H2OStopper': {
                'val': 0,
                'reg': 49169
            },
            'Default': {
                'val': 0,
                'reg': 49170
            }
        }

    }
}

par['FC301'] = {
    'start': False,
    'split': False,
    'H2': 0
}

par['FC301A'] = {
    'Pset': 0,
    'Pread': 0,
    'H2': 1.6,
    'log': '',
    'activated': False,
    'status': 'on'
}

par['FC301B'] = {
    'Pset': 0,
    'Pread': 0,
    'H2': 1.2,
    'log': '',
    'activated': False,
    'status': 'on'
}

par['S201'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

par['S202'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

par['S203'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

par['S204'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

par['S205'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

par['TI306'] = {
    'T': 36
}

par['PI307'] = {
    'pressure': 12.5
}

par['EV'] = {
    '104': True,
    '303': True,
    '103': False,
    '302': False
}

sel_util = False


sim = dict()
sim['EL101'] = {
    'status': 'off',
    'power': 100,
    'pressure': 100,
    'flux': 100
}

sim['S201'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

sim['S202'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

sim['S203'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

sim['S204'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}

sim['S205'] = {
    'pressure': 12.5,
    'Tflux': 36,
    'Tvessel': 36
}
