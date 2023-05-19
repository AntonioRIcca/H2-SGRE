sel_util = False
sel_settings = False
sel_mb = False
mb_conn = False


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

par['TT216'] = {
    'val': 16,
    'mb': {
        'ch': 31,
        'reg': 14,
        'scale': 0.1,
        'offset': 0
    }
}

par['TT217'] = {
    'val': 17,
    'mb': {
        'ch': 31,
        'reg': 15,
        'scale': 0.1,
        'offset': 0
    }
}

par['TT218'] = {
    'val': 18,
    'mb': {
        'ch': 31,
        'reg': 16,
        'scale': 0.1,
        'offset': 0
    }
}

par['TT219'] = {
    'val': 19,
    'mb': {
        'ch': 31,
        'reg': 17,
        'scale': 0.1,
        'offset': 0
    }
}

par['TT220'] = {
    'val': 20,
    'mb': {
        'ch': 31,
        'reg': 18,
        'scale': 0.1,
        'offset': 0
    }
}

par['TT310'] = {
    'val': 31,
    'mb': {
        'ch': 31,
        'reg': 19,
        'scale': 0.1,
        'offset': 0
    }
}

par['TI221'] = {
    'val': 21,
    'mb': {
        'ch': 21,
        'reg': 14,
        'scale': 0.01,
        'offset': 0
    }
}

par['TI222'] = {
    'val': 22,
    'mb': {
        'ch': 21,
        'reg': 15,
        'scale': 0.01,
        'offset': 0
    }
}

par['TI223'] = {
    'val': 23,
    'mb': {
        'ch': 21,
        'reg': 16,
        'scale': 0.01,
        'offset': 0
    }
}

par['TI224'] = {
    'val': 24,
    'mb': {
        'ch': 21,
        'reg': 17,
        'scale': 0.01,
        'offset': 0
    }
}

par['TI225'] = {
    'val': 25,
    'mb': {
        'ch': 21,
        'reg': 18,
        'scale': 0.01,
        'offset': 0
    }
}

par['TI306'] = {
    'val': 36,
    'mb': {
        'ch': 21,
        'reg': 19,
        'scale': 0.01,
        'offset': 0
    }
}

par['PI226'] = {
    'val': 12.6,
    'mb': {
        'ch': 22,
        'reg': 14,
        'scale': 0.0015625,
        'offset': 6.25
    }
}

par['PI227'] = {
    'val': 12.7,
    'mb': {
        'ch': 22,
        'reg': 15,
        'scale': 0.0015625,
        'offset': 6.25
    }
}

par['PI228'] = {
    'val': 12.8,
    'mb': {
        'ch': 22,
        'reg': 16,
        'scale': 0.0015625,
        'offset': 6.25
    }
}

par['PI229'] = {
    'val': 12.9,
    'mb': {
        'ch': 22,
        'reg': 17,
        'scale': 0.0015625,
        'offset': 6.25
    }
}

par['PI230'] = {
    'val': 13.0,
    'mb': {
        'ch': 22,
        'reg': 18,
        'scale': 0.0015625,
        'offset': 6.25
    }
}

par['PI307'] = {
    'val': 10.7,
    'mb': {
        'ch': 22,
        'reg': 19,
        'scale': 0.0015625,
        'offset': 6.25
    }
}

par['EV'] = {
    '103': {
        'val': True,
        'mb': {
            'ch': 12,
            'reg': 18,
        }
    },
    '104': {
        'val': True,
        'mb': {
            'ch': 12,
            'reg': 19,
        }
    },
    '302': {
        'val': False,
        'mb': {
            'ch': 14,
            'reg': 18,
        }
    },
    '303': {
        'val': False,
        'mb': {
            'ch': 14,
            'reg': 19,
        }
    },
}


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


alarm = dict()
alarm['EL101'] = {
    'power': {
        'tr+': 10,
        'tr-': 10,
        'time': 0,
        'on': False
    },
    'pressure': {
        'tr+': 20,
        'tr-': 0,
        'time': 0,
        'on': True
    },
    'H2': {
        'tr+': 100,
        'tr-': 0,
        'time': 0,
        'on': False
    }
}

alarm['FC301A'] = {
    'power': {
        'tr+': 10,
        'tr-': 10,
        'time': 0,
        'on': False
    },
    'pressure': {
        'tr+': 20,
        'tr-': - 100,
        'time': 0,
        'on': False
    },
    'H2': {
        'tr+': 100,
        'tr-': - 100,
        'time': 0,
        'on': False
    }
}

alarm['FC301B'] = {
    'power': {
        'tr+': 10,
        'tr-': 10,
        'time': 0,
        'on': False
    },
    'pressure': {
        'tr+': 20,
        'tr-': - 100,
        'time': 0,
        'on': False
    },
    'H2': {
        'tr+': 100,
        'tr-': - 100,
        'time': 0,
        'on': False
    }
}

dat = dict()
dat[11] = {
    'name': 'DAT 3130',
    'mod': '3130',
    'index': 1,
    'signal': 'd',
    'reg': {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0
    }
}

dat[12] = {
    'name': 'DAT 3130',
    'mod': '3130',
    'index': 2,
    'signal': 'd',
    'reg': {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0
    }
}

dat[13] = {
    'name': 'DAT 3130',
    'mod': '3130',
    'index': 3,
    'signal': 'd',
    'reg': {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0
    }
}

dat[14] = {
    'name': 'DAT 3130',
    'mod': '3130',
    'index': 4,
    'signal': 'd',
    'reg': {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0
    }
}

dat[21] = {
    'name': 'DAT 3017-I',
    'mod': '3017',
    'index': 1,
    'signal': 'i',
    'reg': {
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 55,
        19: 0,
        20: 0,
        21: 0
    }
}

dat[22] = {
    'name': 'DAT 3017-I',
    'mod': '3017',
    'index': 2,
    'signal': 'i',
    'reg': {
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 14,
        21: 0
    }
}

dat[31] = {
    'name': 'DAT 3018',
    'mod': '3018',
    'index': 1,
    'signal': 't',
    'reg': {
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0
    }
}