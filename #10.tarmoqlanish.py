# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:53:02 2021

@author: ASER
"""
# =============================================================================
# 
# cars = ["toyota", "gm", "hyundai", "mazda", "volvo", "porche"]
# for avto in cars:
#     if avto == "gm":
#         print(avto.upper())
#     else:
#         print(avto.title())
# =============================================================================
# =============================================================================
# 
# cars =["toyota", "gm", "hyundai", "mazda", "volvo", "porche"]
# for avto in cars:
#     if avto != "gm":
#         print(avto.upper())
#     else:
#         print(avto.title())
# =============================================================================
# =============================================================================
# 
# ism = input("Ismingiz nima?\n>>>")
# if ism.lower() == "admin":
#         print("Xush kelibsiz Admin! Foydalanuvchilar ro'yhatinii ko'rasizmi?")
# else:
# =============================================================================
# #         print(f"Xush kelibsiz {ism.title()}! ")
# x=float(input("Birinchi sonni kiriting:\n>>>"))
# y=float(input("Ikkinchi sonni kiriting:\n>>>"))
# if x== y: print("Ikkisi ham teng ekan, Dostonbek!")
# =============================================================================
# istalgan_son= int(input("Istalgan sonni kiriting: \n>>>")) 
# if istalgan_son < 0:
#     print("manfiy son")
# else:
#     print("musbat son")
# =============================================================================
# =============================================================================
# 
# son = int(input("istalgan son kiriting: \n>>>"))
# sqrt = son**0.5
# if son >= 0:
#     print(int(sqrt))
# =============================================================================

son = float(input("Istalgan sonni kiriting: "))
print("Son manfiy") if son<0 else print("Son musbat")