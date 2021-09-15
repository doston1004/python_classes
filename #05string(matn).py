# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:33:02 2021

@author: ASER
"""
# =============================================================================
# 
# matn='Men yangi 🌹 sotib oldim'
# print(matn)
# 
# #STRING USTIDA AMALLAR.
# ism='Ahmad'
# print('Mening ismim ' + ism)
# 
# ism='Ahad'
# familiya='Qayyum'
# print(ism+familiya)
# 
# ism='Ahad'
# familiya='Qayyum'
# print(ism+ ' ' + familiya)
# 
# #f-string
# ism='Ahad'
# familiya='Qayyum'
# ism_sharif=f'{ism} {familiya}'
# print(ism_sharif)
# 
# ism='James'
# familiya="Bond"
# print(f'Salom, mening ismim {ism}. Familiyam {familiya}')
# 
# #Maxsus belgilar
# print('hello world')
# print('hello \tworld')
# print('hello \nworld')
# 
# #STRING METODLARI
# 
# ism='Ahad'
# familiya='Qayum'
# ism_sharif=f'{ism} {familiya} '
# print(ism_sharif.upper())
# 
# ism="Ahad"
# familiya="Qayyum"
# ism_sharif=f'{ism} {familiya}'
# print(ism_sharif.lower())
# 
# 
# ism="Ahad"
# familiya="Qayyum"
# ism_sharif=f'{ism} {familiya}'
# print(ism_sharif.title())
# 
# 
# ism="ahad"
# sharif="qayyum"
# ism_sharif=f'{ism} {sharif}'
# print(ism_sharif.title())
# 
# 
# ism="Ahad"
# sharif="Qayum"
# ism_sharif=f'{ism} {sharif}'
# print(ism_sharif.capitalize())
# 
# 
# #strip() lstrip() rstrip() metodlari
# meva="      olma      "
# print(meva.strip())
# print(meva.rstrip())
# print(meva.lstrip())
# print(meva)
# 
# #INPUT - FOYDALANUVCHI BILAN MULOQOT
# ism=input('Ismingiz nima?')
# print('Assalom alekum,' +ism)
# 
# 
# #ism=input("Ismingiz nima?\n>>>")
# #print("Assalom alekum, " +ism.title())
# 
# =============================================================================
#AMALIYOT
kocha="Bog'bon"
mahalla="Sag'bon"
tuman="Bodomzor"
viloyat="Samarqand"
# =============================================================================
# print(kocha+" ko'chasi",mahalla+" mahallasi",tuman+" tumani",viloyat+" viloyati")
# =============================================================================
# =============================================================================
# 
# ism=input("qayerdansiz?\n>>>")
# print("Assalom alekum, " ,ism.capitalize(), "ko'chasidanman")
# =============================================================================
# =============================================================================
# 
# ism=input("Qayeransiz?\n>>>")
# print("Assalom alekum, men", ism.capitalize()," mahallasidanman")
# 
# =============================================================================
# # =============================================================================
# ism=input("Qayerdansiz?\n>>>")
# print("men, " ,ism.capitalize(), 'tumanidanman')
# =============================================================================
# # =============================================================================
# ism=input("Qayerdansiz?\n>>>")
# print("Men" ,ism.capitalize(), "viloyatidanman")
# =============================================================================
manzil=f'{kocha} ko\'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati'
print(manzil)
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
print(manzil.title())
