# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 05:54:01 2021

@author: ASER
"""
# =============================================================================
# 
# son = 78
# if son > 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
# 
# =============================================================================
# =============================================================================
# 
# yosh = int(input("Yoshingiz nechida?\n>>> "))
# if yosh <= 4:
#     narh=0
# elif yosh <= 12:
#     narh=5000
# elif yosh <= 18:
#     narh = 8000
# else: 
#     narh = 10000
#     print(f"Sizga kirish {narh} so'm!")
# =============================================================================
# =============================================================================
# 
# kun = input("Bugun nima kun?\n>>> ")
# if kun.lower() == "yakshanba" or kun.lower() == "shanba":
#     print("bugun dam olish kuni")
# else:
#     print("Bugun ish kuni.")
# =============================================================================
# =============================================================================
# 
# kun = input("Bugun nima kun?\n>>> ")
# havo = float(input("Havo harorati qanday?\n>>> "))
# if kun.lower() == "yakshanba" and havo >= 30:
#     print("Cho'milgani ketdik!")
# elif kun.lower() == "yakshanba" and havo <=30:
#     print("Uyda dam olamiz")
# =============================================================================
# =============================================================================
# 
# narh = 15000
# choy = True
# salat = True
# 
# if choy and salat:
#     narh= narh + 10000
# elif choy or salat:
#     narh = narh +5000
# print(f"Jami {narh} so'm.")
# =============================================================================
# =============================================================================
# 
# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 0
# 
# if choy:
#     print("Mijoz choy sotib oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat sotib oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi")
#     narh = narh + 4000
# if kompot:
#     print("Mijoz kompot sotib oldi.")
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti sotib oldi.")
#     narh = narh + 5000
# print(f"Jami {narh}")
# =============================================================================

menu = ["manti", "osh", "qozonkabob", "shashlik", "norin",  ]
ovqat = input("Nima ovqat yeysiz?\n>>>")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bizda bunday taom yo'q")