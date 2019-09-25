samples_path = '/nfs/scratch/fynu/fbury/MoMEMta_output/'

#################### Valid weights #########################
samples_dict = {}

# HToZA #
samples_dict['HToZA'] = [
                            #########################   Background weights regression  ###########################
                            #'valid_weights/HToZATo2L2B_MH-1000_MA-200.root',
                            #'valid_weights/HToZATo2L2B_MH-1000_MA-500.root',
                            #'valid_weights/HToZATo2L2B_MH-1000_MA-50.root',
                            #'valid_weights/HToZATo2L2B_MH-2000_MA-1000.root',
                            #'valid_weights/HToZATo2L2B_MH-200_MA-100.root',
                            #'valid_weights/HToZATo2L2B_MH-200_MA-50.root',
                            #'valid_weights/HToZATo2L2B_MH-250_MA-100.root',
                            #'valid_weights/HToZATo2L2B_MH-250_MA-50.root',
                            #'valid_weights/HToZATo2L2B_MH-3000_MA-2000.root',
                            #'valid_weights/HToZATo2L2B_MH-300_MA-100.root',
                            #'valid_weights/HToZATo2L2B_MH-300_MA-200.root',
                            #'valid_weights/HToZATo2L2B_MH-300_MA-50.root',
                            #'valid_weights/HToZATo2L2B_MH-500_MA-100.root',
                            #'valid_weights/HToZATo2L2B_MH-500_MA-200.root',
                            #'valid_weights/HToZATo2L2B_MH-500_MA-300.root',
                            #'valid_weights/HToZATo2L2B_MH-500_MA-400.root',
                            #'valid_weights/HToZATo2L2B_MH-500_MA-50.root',
                            #'valid_weights/HToZATo2L2B_MH-650_MA-50.root',
                            #'valid_weights/HToZATo2L2B_MH-800_MA-100.root',
                            #'valid_weights/HToZATo2L2B_MH-800_MA-200.root',
                            #'valid_weights/HToZATo2L2B_MH-800_MA-400.root',
                            #'valid_weights/HToZATo2L2B_MH-800_MA-50.root',
                            #'valid_weights/HToZATo2L2B_MH-800_MA-700.root',
                            
                            ##########################  Signal weights regression  ############################
                            #'signal_weights_valid/HToZATo2L2B_MH-1000_MA-200_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-1000_MA-500_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-1000_MA-50_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-2000_MA-1000_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-200_MA-100_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-200_MA-50_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-250_MA-100_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-250_MA-50_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-3000_MA-2000_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-300_MA-100_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-300_MA-200_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-300_MA-50_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-500_MA-100_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-500_MA-200_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-500_MA-300_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-500_MA-400_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-500_MA-50_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-650_MA-50_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-800_MA-100_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-800_MA-200_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-800_MA-400_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-800_MA-50_signal_weights.root',
                            #'signal_weights_valid/HToZATo2L2B_MH-800_MA-700_signal_weights.root',

                            ###############################  Classification  ##################################
                            #'classification_weights_valid/HToZATo2L2B_MH-1000_MA-200_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-1000_MA-500_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-1000_MA-50_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-2000_MA-1000_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-200_MA-100_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-200_MA-50_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-250_MA-100_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-250_MA-50_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-3000_MA-2000_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-300_MA-100_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-300_MA-200_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-300_MA-50_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-500_MA-100_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-500_MA-200_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-500_MA-300_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-500_MA-400_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-500_MA-50_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-650_MA-50_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-800_MA-100_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-800_MA-200_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-800_MA-400_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-800_MA-50_all_weights.root',
                            #'classification_weights_valid/HToZATo2L2B_MH-800_MA-700_all_weights.root',

                            ######################  Classification with both weight and output  ################
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-1000_MA-200_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-1000_MA-500_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-1000_MA-50_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-2000_MA-1000_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-200_MA-100_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-200_MA-50_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-250_MA-100_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-250_MA-50_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-3000_MA-2000_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-300_MA-100_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-300_MA-200_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-300_MA-50_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-100_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-200_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-300_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-400_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-50_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-650_MA-50_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-100_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-200_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-400_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-50_all_weights.root',
                            #'signal_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-700_all_weights.root',



                        ]
# TT bar #
samples_dict['TT'] = [
                            #########################   Background weights regression  ###########################
                            #'valid_weights/TT_Other.root',
                            #'valid_weights/TTTo2L2Nu_partial.root', # We don't need the full sample 

                            ##########################  Signal weights regression  ############################
                            #'signal_weights_valid/TT_Other_signal_weights.root',
                            #'signal_weights_valid/TTTo2L2Nu_signal_weights.root', 

                            ###############################  Classification  ##################################
                            #'classification_weights_valid/TT_Other_all_weights.root',
                            #'classification_weights_valid/TTTo2L2Nu_all_weights.root',

                            ######################  Classification with both weight and output  ################
                            #'signal_regression_for_classification_weights/TT_Other_all_weights.root',
                            #'signal_regression_for_classification_weights/TTTo2L2Nu_all_weights.root',
                            
                            ############################## Matrix Element ######################################
                            #'ME_TTBar/TT_Other_ME.root',
                            #'ME_TTBar/TTTo2L2Nu_ME.root',
                            'ME_TTBar/TTTo2L2Nu_ME_test.root',
                            
                      ]

# Drell-Yann #
samples_dict['DY'] = [
                            #########################   Background weights regression  ###########################
                            #'valid_weights/DYJetsToLL_M.root',
                            #'valid_weights/DYToLL_0J.root',
                            #'valid_weights/DYToLL_1J.root',
                            #'valid_weights/DYToLL_2J.root',

                            ##########################  Signal weights regression  ############################
                            #'signal_weights_valid/DYJetsToLL_M_signal_weights.root',
                            #'signal_weights_valid/DYToLL_0J_signal_weights.root',
                            #'signal_weights_valid/DYToLL_1J_signal_weights.root',
                            #'signal_weights_valid/DYToLL_2J_signal_weights.root',

                            ###############################  Classification  ##################################
                            #'classification_weights_valid/DYJetsToLL_M_all_weights.root',
                            #'classification_weights_valid/DYToLL_0J_all_weights.root',
                            #'classification_weights_valid/DYToLL_1J_all_weights.root',
                            #'classification_weights_valid/DYToLL_2J_all_weights.root',

                            ######################  Classification with both weight and output  ################
                            #'signal_regression_for_classification_weights/DYJetsToLL_M_all_weights.root',
                            #'signal_regression_for_classification_weights/DYToLL_0J_all_weights.root',
                            #'signal_regression_for_classification_weights/DYToLL_1J_all_weights.root',
                            #'signal_regression_for_classification_weights/DYToLL_2J_all_weights.root',

                            ############################## Matrix Element ######################################
                            #'ME_TTBar/DYJetsToLL_M-10to50_ME.root',
                            #'ME_TTBar/DYToLL_0J_ME.root',
                            #'ME_TTBar/DYToLL_1J_ME.root',
                            #'ME_TTBar/DYToLL_2J_ME.root',
                            'ME_TTBar/DYToLL_0J_ME_test.root',
                      ]


#################### Invalid DY weights #########################
samples_dict['invalid_DY'] = [
                            'invalid_DY_weights_recomputed/DYToLL_1J_invalid_DY.root',
                            'invalid_DY_weights_recomputed/DYToLL_2J_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-250_MA-50_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-3000_MA-2000_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-300_MA-200_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-300_MA-50_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-500_MA-300_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-500_MA-400_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-500_MA-50_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-800_MA-50_invalid_DY.root',
                            'invalid_DY_weights_recomputed/HToZATo2L2B_MH-800_MA-700_invalid_DY.root',
                            'invalid_DY_weights_recomputed/TTTo2L2Nu_invalid_DY.root',
                             ]

#################### Invalid TT weights #########################
samples_dict['invalid_TT'] = [
                            'invalid_TT_weights_recomputed/DYJetsToLL_M_invalid_TT.root',
                            'invalid_TT_weights_recomputed/DYToLL_1J_invalid_TT.root',
                            'invalid_TT_weights_recomputed/DYToLL_2J_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-1000_MA-200_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-1000_MA-500_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-1000_MA-50_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-2000_MA-1000_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-250_MA-50_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-3000_MA-2000_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-300_MA-100_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-300_MA-200_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-300_MA-50_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-500_MA-100_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-500_MA-200_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-500_MA-300_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-500_MA-400_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-500_MA-50_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-650_MA-50_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-800_MA-100_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-800_MA-200_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-800_MA-400_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-800_MA-50_invalid_TT.root',
                            'invalid_TT_weights_recomputed/HToZATo2L2B_MH-800_MA-700_invalid_TT.root',
                            'invalid_TT_weights_recomputed/TT_Other_invalid_TT.root',
                            'invalid_TT_weights_recomputed/TTTo2L2Nu_invalid_TT.root',
                            ]
                                                         
#################### JEC weights #########################
samples_dict['JEC'] = [
                            'JEC/DYJetsToLL_M-10to50_JEC.root',
                            'JEC/DYToLL_0J_JEC.root',
                            'JEC/DYToLL_1J_JEC.root',
                            'JEC/DYToLL_2J_JEC.root',
                            'JEC/TT_Other_JEC.root',
                            'JEC/TTTo2L2Nu_JEC.root',
]
############### interpolation weights ####################
samples_dict['interpolation'] = [
                                    'interpolation_weights/all_weights/DYJetsToLL_M_interpolation_new.root',
                                    'interpolation_weights/all_weights/DYToLL_0J_interpolation_new.root',
                                    'interpolation_weights/all_weights/DYToLL_1J_interpolation_new.root',
                                    'interpolation_weights/all_weights/DYToLL_2J_interpolation_new.root',
                                    #'interpolation_weights/all_weights/HToZATo2L2B_MH-1000_MA-200_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-1000_MA-500_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-1000_MA-50_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-2000_MA-1000_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-200_MA-100_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-200_MA-50_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-250_MA-100_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-250_MA-50_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-3000_MA-2000_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-300_MA-100_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-300_MA-200_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-300_MA-50_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-500_MA-100_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-500_MA-200_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-500_MA-300_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-500_MA-400_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-500_MA-50_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-650_MA-50_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-800_MA-100_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-800_MA-200_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-800_MA-400_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-800_MA-50_interpolation_new.root',
                                    'interpolation_weights/all_weights/HToZATo2L2B_MH-800_MA-700_interpolation_new.root',
                                    'interpolation_weights/all_weights/TT_Other_interpolation_new.root',
                                    'interpolation_weights/all_weights/TTTo2L2Nu_interpolation_new.root',

                                ]

samples_dict['back_regression_for_classification'] = [
                            'classification_weights_valid/HToZATo2L2B_MH-1000_MA-200_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-1000_MA-500_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-1000_MA-50_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-2000_MA-1000_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-200_MA-100_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-200_MA-50_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-250_MA-100_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-250_MA-50_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-3000_MA-2000_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-300_MA-100_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-300_MA-200_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-300_MA-50_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-500_MA-100_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-500_MA-200_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-500_MA-300_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-500_MA-400_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-500_MA-50_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-650_MA-50_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-800_MA-100_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-800_MA-200_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-800_MA-400_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-800_MA-50_all_weights.root',
                            'classification_weights_valid/HToZATo2L2B_MH-800_MA-700_all_weights.root',
                            'classification_weights_valid/DYJetsToLL_M_all_weights.root',
                            'classification_weights_valid/DYToLL_0J_all_weights.root',
                            'classification_weights_valid/DYToLL_1J_all_weights.root',
                            'classification_weights_valid/DYToLL_2J_all_weights.root',
                            'classification_weights_valid/TT_Other_all_weights.root',
                            'classification_weights_valid/TTTo2L2Nu_all_weights.root',
                            ]

samples_dict['signal_regression_for_classification'] = [
                           'back_regression_for_classification_weights/DYJetsToLL_M_all_weights.root',
                           'back_regression_for_classification_weights/DYToLL_0J_all_weights.root',
                           'back_regression_for_classification_weights/DYToLL_1J_all_weights.root',
                           'back_regression_for_classification_weights/DYToLL_2J_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-1000_MA-200_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-1000_MA-500_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-1000_MA-50_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-2000_MA-1000_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-200_MA-100_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-200_MA-50_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-250_MA-100_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-250_MA-50_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-3000_MA-2000_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-300_MA-100_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-300_MA-200_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-300_MA-50_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-100_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-200_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-300_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-400_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-500_MA-50_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-650_MA-50_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-100_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-200_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-400_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-50_all_weights.root',
                           'back_regression_for_classification_weights/HToZATo2L2B_MH-800_MA-700_all_weights.root',
                           'back_regression_for_classification_weights/TT_Other_all_weights.root',
                           'back_regression_for_classification_weights/TTTo2L2Nu_all_weights.root',
                           ]


