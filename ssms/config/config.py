from ssms.basic_simulators import boundary_functions as bf
import numpy as np

model_config = {'ddm': {'name': 'ddm',
                        'params':['v', 'a', 'z', 't'],
                        'param_bounds': [[-3.0, 0.3, 0.1, 0.0], [3.0, 2.5, 0.9, 2.0]],
                        'boundary': bf.constant,
                        'n_params': 4,
                        'default_params': [0.0, 1.0, 0.5, 1e-3],
                        'hddm_include': ['z'],
                        'nchoices': 2},
                'angle':{'name': 'angle',
                        'params': ['v', 'a', 'z', 't', 'theta'],
                         'param_bounds': [[-3.0, 0.3, 0.2, 1e-3, -0.1], [3.0, 2.0, 0.8, 2.0, 1.45]],
                        'boundary': bf.angle,
                        'n_params': 5,
                        'default_params': [0.0, 1.0, 0.5, 1e-3, 0.0],
                        'hddm_include':['z', 'theta'],
                        'nchoices': 2},
                'weibull':{'name': 'weibull',
                           'params': ['v', 'a', 'z', 't', 'alpha', 'beta'],
                           'param_bounds': [[-2.5, 0.3, 0.2, 1e-3, 0.31, 0.31], [2.5, 2.5, 0.8, 2.0, 4.99, 6.99]],
                           'boundary': bf.weibull_cdf,
                           'n_params': 6,
                           'default_params': [0.0, 1.0, 0.5, 1e-3, 3.0, 3.0],
                           'hddm_include': ['z', 'alpha', 'beta'],
                           'nchoices': 2},
                'levy':{'name': 'levy',
                        'params':['v', 'a', 'z', 'alpha', 't'],
                        'param_bounds':[[-3.0, 0.3, 0.1, 1.0, 1e-3], [3.0, 2.0, 0.9, 2.0, 2]],
                        'boundary': bf.constant,
                        'n_params': 5,
                        'default_params': [0.0, 1.0, 0.5, 1.5, 1e-3],
                        'hddm_include': ['z', 'alpha'],
                        'nchoices': 2},
                'full_ddm':{'name': 'full_ddm',
                            'params':['v', 'a', 'z', 't', 'sz', 'sv', 'st'],
                            'param_bounds':[[-3.0, 0.3, 0.3, 0.25, 1e-3, 1e-3, 1e-3], [3.0, 2.5, 0.7, 2.25, 0.2, 2.0, 0.25]],
                            'boundary': bf.constant,
                            'n_params': 7,
                            'default_params': [0.0, 1.0, 0.5, 0.25, 1e-3, 1e-3, 1e-3],
                            'hddm_include': ['z', 'st', 'sv', 'sz'],
                            'nchoices': 2},
                'ornstein':{'name': 'ornstein', 
                            'params':['v', 'a', 'z', 'g', 't'],
                            'param_bounds':[[-2.0, 0.3, 0.2, -1.0, 1e-3], [2.0, 2.0, 0.8, 1.0, 2]],
                            'boundary': bf.constant,
                            'n_params': 5,
                            'default_params': [0.0, 1.0, 0.5, 0.0, 1e-3],
                            'hddm_include': ['z', 'g'],
                            'nchoices': 2},
                'ddm_sdv':{'name': 'ddm_sdv',
                           'params':['v', 'a', 'z', 't', 'sv'],
                           'param_bounds':[[-3.0, 0.3, 0.1, 1e-3, 1e-3],[ 3.0, 2.5, 0.9, 2.0, 2.5]],
                           'boundary': bf.constant,
                           'n_params': 5,
                           'default_params': [0.0, 1.0, 0.5, 1e-3, 1e-3],
                           'hddm_include': ['z', 'sv'],
                           'nchoices': 2
                           },
                "race_3":{'name': 'race_3',
                          'params': ["v0", "v1", "v2", "a", "z0", "z1", "z2", "ndt"],
                          'param_bounds': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [2.5, 2.5, 2.5, 3.0, 0.9, 0.9, 0.9, 2.0]],
                          'boundary': bf.constant,
                          'n_params': 8,
                          'default_params': [0.0, 0.0, 0.0, 2.0, 0.5, 0.5, 0.5, 1e-3],
                          'hddm_include': ["v0", "v1", "v2", "a", "z0", "z1", "z2", "ndt"],
                          'nchoices': 3
                          },
                "race_no_bias_3":{'name': 'race_no_bias_3',
                          'params': ["v0", "v1", "v2", "a", "z", "ndt"],
                          'param_bounds': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [2.5, 2.5, 2.5, 3.0, 0.9, 2.0]],
                          'boundary': bf.constant,
                          'n_params': 6,
                          'default_params': [0.0, 0.0, 0.0, 2.0, 0.5, 1e-3],
                          'hddm_include': ["v0", "v1", "v2", "a", "z0", "z1", "z2", "ndt"],
                          'nchoices': 3
                          },
                "race_no_bias_angle_3": {'name': 'race_no_bias_angle_3',
                                        'params': ["v0", "v1", "v2", "a", "z", "ndt", "theta"],
                                        'param_bounds': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.1], [2.5, 2.5, 2.5, 3.0, 0.9, 2.0, 1.45]],
                                        'boundary': bf.angle,
                                        'n_params': 7,
                                        'default_params': [0.0, 0.0, 0.0, 2.0, 0.5, 1e-3, 0.0],
                                        'hddm_include': ["v0", "v1", "v2", "a", "z", "ndt", "theta"],
                                        'nchoices': 3
                                        },                     
                "race_4":{'name': 'race_4',
                          'params': ["v0", "v1", "v2","v3", "a", "z0", "z1", "z2", "z3", "ndt"],
                          'param_bounds': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 0.9, 0.9, 0.9, 2.0]],
                          'boundary': bf.constant,
                          'n_params': 10,
                          'default_params': [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 0.5, 0.5, 0.5, 1e-3],
                          'hddm_include': ["v0", "v1", "v2", "a", "z0", "z1", "z2", "ndt"],
                          'nchoices': 4
                          },
                "race_no_bias_4":{'name': 'race_no_bias_4',
                          'params': ["v0", "v1", "v2","v3", "a", "z", "ndt"],
                          'param_bounds': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 2.0]],
                          'boundary': bf.constant,
                          'n_params': 7,
                          'default_params': [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 1e-3],
                          'hddm_include': ["v0", "v1", "v2", "a", "z", "ndt"],
                          'nchoices': 4
                          },
                "race_no_bias_angle_4":{'name': 'race_no_bias_angle_4',
                          'params': ["v0", "v1", "v2","v3", "a", "z", "ndt", "theta"],
                          'param_bounds': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.1], [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 2.0, 1.45]],
                          'boundary': bf.angle,
                          'n_params': 8,
                          'default_params': [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 1e-3, 0.0],
                          'hddm_include': ["v0", "v1", "v2", "a", "z", "ndt", "theta"],
                          'nchoices': 4
                          },
                "lca_3": {'name': 'lca_3',
                          'params': ['v0', 'v1', 'v2', 'a', 'z0', 'z1', 'z2', 'g', 'b', 'ndt'],
                          'param_bounds': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0], [2.5, 2.5, 2.5, 3.0, 0.9, 0.9, 0.9, 1.0, 1.0, 2.0]],
                          'boundary': bf.constant,
                          'n_params': 10,
                          'default_params': [0.0, 0.0, 0.0, 2.0, 0.5, 0.5, 0.5, 0.0, 0.0, 1e-3],
                          'hddm_include': ['v0', 'v1', 'v2', 'a', 'z0', 'z1', 'z2', 'g', 'b', 'ndt'],
                          'nchoices': 3
                          },
                "lca_no_bias_3": {'name': 'lca_no_bias_3',
                                  'params': ['v0', 'v1', 'v2', 'a', 'z', 'g', 'b', 'ndt'],
                                  'param_bounds': [[0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0],[2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0]],
                                  'boundary': bf.constant,
                                  'n_params': 8,
                                  'default_params': [0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3],
                                  'hddm_include': ['v0', 'v1', 'v2', 'a', 'z', 'g', 'b', 'ndt'],
                                  'nchoices': 3
                                  },
                "lca_no_bias_angle_3": {'name': 'lca_no_bias_angle_3',
                                        'params': ['v0', 'v1', 'v2', 'a', 'z', 'g', 'b', 'ndt', 'theta'],
                                        'param_bounds': [[0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0, -1.0], [2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0, 1.45]],
                                        'boundary': bf.angle,
                                        'n_params': 9,
                                        'default_params': [0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3, 0.0],
                                        'hddm_include': ['v0', 'v1', 'v2', 'a', 'z', 'g', 'b', 'ndt', 'theta'],
                                        'nchoices': 3
                                        },                       
                "lca_4": {'name': 'lca_4',
                          'params': ['v0', 'v1', 'v2', 'v3',  'a', 'z0', 'z1', 'z2', 'z3', 'g', 'b', 'ndt'],
                          'param_bounds': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0], [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 0.9, 0.9, 0.9, 1.0, 1.0, 2.0]],
                          'boundary': bf.constant,
                          'n_params': 12,
                          'default_params': [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 1e-3],
                          'hddm_include': ['v0', 'v1', 'v2', 'v3', 'a', 'z0', 'z1', 'z2', 'z3', 'g', 'b', 'ndt'],
                          'nchoices': 4
                          },
                "lca_no_bias_4": {'name': 'lca_no_bias_4',
                                  'params': ['v0', 'v1', 'v2', 'v3', 'a', 'z', 'g', 'b', 'ndt'],
                                  'param_bounds': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0], [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0]],
                                  'boundary': bf.constant,
                                  'n_params': 9,
                                  'default_params': [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3],
                                  'hddm_include': ['v0', 'v1', 'v2', 'v3', 'a', 'z', 'g', 'b', 'ndt'],
                                  'nchoices': 4
                                  },
                "lca_no_bias_angle_4": {'name': 'lca_no_bias_angle_4',
                                        'params': ['v0', 'v1', 'v2', 'v3', 'a', 'z', 'g', 'b', 'ndt', 'theta'],
                                        'param_bounds': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0, -.1], [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0, 1.45]], #[[0, 2.5], [0, 2.5], [0, 2.5], [0, 2.5], [1.0, 3.0], [0.1, 0.9], [-1.0, 1.0], [-1.0, 1.0], [0.0, 2.0], [-.1, 1.45]],
                                        'boundary': bf.angle,
                                        'n_params': 10,
                                        'default_params': [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3, 0.0],
                                        'hddm_include': ['v0', 'v1', 'v2', 'v3', 'a', 'z', 'g', 'b', 'ndt', 'theta'],
                                        'nchoices': 4
                                        },
                'ddm_par2': {'name': 'ddm_par2',
                             'params': ['vh', 'vl1', 'vl2', 'a', 'zh', 'zl1', 'zl2', 't'],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.2, 0.2, 0.2, 0.0], [2.5, 2.5, 2.5, 2.0, 0.8, 0.8, 0.8, 2.0]],
                             'boundary': bf.constant,
                             'n_params': 8,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 1.0],
                             'hddm_include': ['vh', 'vl1', 'vl2', 'a', 'zh', 'zl1', 'zl2', 't'],
                             'nchoices': 4,
                            },
                'ddm_seq2': {'name': 'ddm_seq2',
                             'params': ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.2, 0.2, 0.2, 0.0], [2.5, 2.5, 2.5, 2.0, 0.8, 0.8, 0.8, 2.0]],
                             'boundary': bf.constant,
                             'n_params': 8,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 1.0],
                             'hddm_include': ['vh', 'vl1', 'vl2', 'a', 'zh', 'zl1', 'zl2', 't'],
                             'nchoices': 4,
                            },
                'ddm_mic2': {'name': 'ddm_mic2',
                             'params': ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t"],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.2, 0.2, 0.2, 0.0, 0.0], [2.5, 2.5, 2.5, 2.0, 0.8, 0.8, 0.8, 1.0, 2.0]],
                             'boundary': bf.constant,
                             'n_params': 9,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5],
                             'hddm_include': ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t"],
                             'nchoices': 4,
                            },
                'ddm_par2_no_bias': {'name': 'ddm_par2_no_bias',
                             'params': ['vh', 'vl1', 'vl2', 'a', 't'],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.0], [2.5, 2.5, 2.5, 2.0, 2.0]],
                             'boundary': bf.constant,
                             'n_params': 5,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 1.0],
                             'hddm_include': ['vh', 'vl1', 'vl2', 'a', 'zh', 'zl1', 'zl2', 't'],
                             'nchoices': 4,
                            },
                'ddm_seq2_no_bias': {'name': 'ddm_seq2_no_bias',
                             'params': ["vh", "vl1", "vl2", "a", "t"],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.0], [2.5, 2.5, 2.5, 2.0, 2.0]],
                             'boundary': bf.constant,
                             'n_params': 5,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 1.0],
                             'hddm_include': ['vh', 'vl1', 'vl2', 'a', 'zh', 'zl1', 'zl2', 't'],
                             'nchoices': 4,
                            },
                'ddm_mic2_no_bias': {'name': 'ddm_mic2_no_bias',
                             'params': ["vh", "vl1", "vl2", "a", "d", "t"],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.0, 0.0], [2.5, 2.5, 2.5, 2.0, 1.0, 2.0]],
                             'boundary': bf.constant,
                             'n_params': 6,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 0.5, 1.0],
                             'hddm_include': ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t"],
                             'nchoices': 4,
                            },
                'ddm_par2_angle_no_bias': {'name': 'ddm_par2_angle_no_bias',
                             'params': ['vh', 'vl1', 'vl2', 'a', 't', 'theta'],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.0, -0.1], [2.5, 2.5, 2.5, 2.0, 2.0, 1.45]],
                             'boundary': bf.angle,
                             'n_params': 6,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 1.0, 0.0],
                             'hddm_include': ['vh', 'vl1', 'vl2', 'a', 'zh', 'zl1', 'zl2', 't', 'theta'],
                             'nchoices': 4,
                            },
                'ddm_seq2_angle_no_bias': {'name': 'ddm_seq2_angle_no_bias',
                             'params': ["vh", "vl1", "vl2", "a", "t", 'theta'],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.0, -0.1], [2.5, 2.5, 2.5, 2.0, 2.0, 1.45]],
                             'boundary': bf.angle,
                             'n_params': 6,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 1.0, 0.0],
                             'hddm_include': ['vh', 'vl1', 'vl2', 'a', 'zh', 'zl1', 'zl2', 't', 'theta'],
                             'nchoices': 4,
                            },
                'ddm_mic2_angle_no_bias': {'name': 'ddm_mic2_angle_no_bias',
                             'params': ["vh", "vl1", "vl2", "a", "d", "t", 'theta'],
                             'param_bounds': [[-2.5, -2.5, -2.5, 0.3, 0.0, 0.0, -0.1], [2.5, 2.5, 2.5, 2.0, 1.0, 2.0, 1.45]],
                             'boundary': bf.angle,
                             'n_params': 7,
                             'default_params': [0.0, 0.0, 0.0, 1.0, 0.5, 1.0, 0.0],
                             'hddm_include': ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t", "theta"],
                             'nchoices': 4,
                            },
                'glob':{'name': 'glob',
                        'params': ['v', 'a', 'z', 'alphar', 'g', 't', 'theta'],
                        'param_bounds': [[-3.0, 0.3, 0.15, 1.0, -1.0, 1e-5, -0.0], [3.0, 2.0, 0.85, 2.0, 1.0, 2.0, 1.45]],
                        'n_params': 7,
                        'default_params': [0.0, 1.0, 0.5, 2.0, 0.0, 1.0, 0.0],
                        'hddm_include': ['z', 'alphar', 'g', 'theta'],
                        'nchoices': 2,
                        'components': {'names': ['g', 'alphar', 'theta'],
                                        'off_values': np.float32(np.array([0, 1, 0])),
                                        'probabilities': np.array([1/3, 1/3, 1/3]),
                                        'labels': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
                                        'n_components': 3,
                                        },
                        # 'components': {'g': {'label_component': np.float32(np.array([1, 0, 0])),
                        #                      'off_value': 0,
                        #                      'probability': 1/3},
                        #                'alphar': {'label_component': np.float32(np.array([0, 1, 0])),
                        #                           'off_value': 1,
                        #                           'probability': 1/3},
                        #                'theta': {'label_component': np.float32(np.array([0, 0, 1])),
                        #                          'off_value': 0,
                        #                          'probability': 1/3}
                        #                }
                        },
                }

model_config['weibull_cdf'] = model_config['weibull'].copy()
model_config['full_ddm2'] = model_config['full_ddm'].copy()


#### DATASET GENERATOR CONFIGS ----------------------------------------------------------------

kde_simulation_filters = {'mode': 20, # != (if mode is max_rt)
                          'choice_cnt': 5, # > (each choice receive at least 10 samples in simulator)
                          'mean_rt': 15, # < (mean_rt is smaller than specified value
                          'std': 0, # > (std is positive for each choice)
                          'mode_cnt_rel': 0.6  # < (mode does not receive more than a proportion of samples for each choice)
                         }

data_generator_config = {'lan': {'mlp': {'output_folder': 'data/lan_mlp/',
                                        'dgp_list': 'ddm', # should be ['ddm'],
                                        'nbins': 0,
                                        'n_samples': 100000,  # eventually should be {'low': 100000, 'high': 100000},
                                        'n_parameter_sets': 10000,
                                        'n_parameter_sets_rejected': 100,
                                        'n_training_samples_by_parameter_set': 1000,
                                        'max_t': 20.0,
                                        'delta_t': 0.001,
                                        'pickleprotocol': 4,
                                        'n_cpus': 'all',
                                        'kde_data_mixture_probabilities': [0.8, 0.1, 0.1],
                                        'simulation_filters': kde_simulation_filters,
                                        'negative_rt_cutoff': -66.77497,
                                        'n_subruns': 10,
                                        'bin_pointwise': False,
                                        'separate_response_channels': False
                                        },
                                 'cnn': {'output_folder': 'data/lan_cnn/',
                                        'dgp_list':'ddm', # should be  ['ddm'],
                                        'n_samples': 100000, # eventually should be  {'low': 100000, 'high': 100000},
                                        'n_parameter_sets': 10000,
                                        'n_parameter_set_rejected': 100, # not used for CNNs
                                        'n_training_samples_by_parameter_set': 1000, # not necessary for CNNs
                                        'nbins': 512,
                                        'max_t': 20.0,
                                        'delta_t': 0.001,
                                        'pickleprotocol': 4,
                                        'n_cpus': 'all',
                                        'simulation_filters': kde_simulation_filters, # not used for CNNs
                                        'negative_rt_cutoff': -66.77497,
                                        'n_subruns': 10,
                                        'bin_pointwise': False,
                                        'separate_response_channels': False,
                                        },
                                 },
                        'ratio_estimator': {'output_folder': 'data/ratio/',
                                            'dgp_list': ['ddm'],
                                            'nbins': 0,
                                            'n_samples': {'low': 100000, 'high': 100000},
                                            'n_parameter_sets': 100000,
                                            'n_parameter_sets_rejected': 100,
                                            'n_training_samples_by_parameter_set': 1000,
                                            'max_t': 20.0,
                                            'delta_t': 0.001,
                                            'pickleprotocol': 4,
                                            'n_cpus': 'all',
                                            'n_subdatasets': 12,
                                            'n_trials_per_dataset': 10000, # EVEN NUMBER ! AF-TODO: Saveguard against odd in code
                                            'kde_data_mixture_probabilities': [0.8, 0.1, 0.1],
                                            'simulation_filters': kde_simulation_filters,
                                            'negative_rt_cutoff': -66.77497,
                                            'n_subruns': 10,
                                            'bin_pointwise': False,
                                            'separate_response_channels': False,
                                            },
                        'defective_detector':{'output_folder': 'data/ratio/',
                                             'dgp_list': ['ddm'],
                                             'nbins': 0,
                                             'n_samples': {'low': 100000, 'high': 100000},
                                             'n_parameter_sets': 100000,
                                             'n_parameter_sets_rejected': 100,
                                             'n_training_samples_by_parameter_set': 1000,
                                             'max_t': 20.0,
                                             'delta_t': 0.001,
                                             'pickleprotocol': 4,
                                             'n_cpus': 'all',
                                             'n_subdatasets': 12,
                                             'n_trials_per_dataset': 10000, # EVEN NUMBER ! AF-TODO: Saveguard against odd in code
                                             'kde_data_mixture_probabilities': [0.8, 0.1, 0.1],
                                             'simulation_filters': kde_simulation_filters,
                                             'negative_rt_cutoff': -66.77497,
                                             'n_subruns': 10,
                                             'bin_pointwise': False,
                                             'separate_response_channels': False,
                                             },
}
##### -------------------------------------------------------------------------------------------