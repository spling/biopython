#!/usr/bin/env python

# This file generated by a program. do not edit.
import Bio.EUtils.POM

#     
#                 This is the Current DTD for Entrez eSearch
# $Id: eSearch_020511.py,v 1.4 2007-07-21 14:55:33 mdehoon Exp $
# 
#  ================================================================= 
class Count(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class RetMax(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class RetStart(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class Id(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class From(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class To(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Term(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Field(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class QueryKey(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class WebEnv(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class Explode(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (Y|N) 
class OP(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (AND|OR|NOT|RANGE|GROUP) 
class IdList(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [(u'Id', u'*')], ''))


class Translation(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel((u',', [(u'From', ''), (u'To', '')], ''))


class TranslationSet(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [(u'Translation', u'*')], ''))


class TermSet(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel((u',', [(u'Term', ''), (u'Field', ''), (u'Count', ''), (u'Explode', '')], ''))


class TranslationStack(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [(u'|', [(u'TermSet', ''), (u'OP', '')], u'*')], ''))


#  Error message tags  
class ERROR(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class OutputMessage(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class QuotedPhraseNotFound(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class PhraseIgnored(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class FieldNotFound(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class PhraseNotFound(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class QueryTranslation(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class ErrorList(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel((u',', [(u'PhraseNotFound', u'*'), (u'FieldNotFound', u'*')], ''))


class WarningList(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel((u',', [(u'PhraseIgnored', u'*'), (u'QuotedPhraseNotFound', u'*'), (u'OutputMessage', u'*')], ''))


#  Response tags 
class eSearchResult(Bio.EUtils.POM.ElementNode):
	CONTENTMODEL = Bio.EUtils.POM.ContentModel((u',', [(u'|', [(u',', [(u'Count', ''), (u',', [(u'RetMax', ''), (u'RetStart', ''), (u'QueryKey', u'?'), (u'WebEnv', u'?'), (u'IdList', ''), (u'TranslationSet', ''), (u'TranslationStack', u'?'), (u'QueryTranslation', '')], u'?')], ''), (u'ERROR', '')], ''), (u'ErrorList', u'?'), (u'WarningList', u'?')], ''))

