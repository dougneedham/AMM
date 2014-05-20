import argparse
import pandas as pd
import math
import sys
parser = argparse.ArgumentParser(description='Read a CSV and generate documentation')
parser.add_argument('--filename', 
                   help='an input file for reading as a CSV')
parser.add_argument('--project', 
                   help='The name of the project')				   
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("--basedocname",help="The name of the document, the table name will be added at the end")					
args = parser.parse_args()
print args.filename
df = pd.read_csv(args.filename)
df.fillna('')
documents = df['TABLE_NAME'].unique()
#print df
def create_file(filename):
# use the filename parsed from the csv file to create a word document returning a file_handle
	opened_file = open(filename,'w')
	return opened_file
def Write_XSD():
	print '<?xml version="1.0" encoding="UTF-8"?>'
	print '<map:Mapping version="1.0" xmlns:map="www.analytixds.com/amm/xml/mapping">'
	print '<map:MappingDetails>'	
	
def Write_Overview(mapping_name,description):
	print '<map:Overview>'
	print '<map:SpecificationName>'+mapping_name + '</map:SpecificationName>'
	print '<map:MapSpecVersion>1</map:MapSpecVersion>'
	print '<map:VersionLabel> </map:VersionLabel>'
	print '<map:JobNameXRef xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:MappingDescription>'+ description +'</map:MappingDescription>'
	print '<map:CreatedBy>Administrator</map:CreatedBy>'
	print '<map:CreatedDateTime>2014-05-15 11:06:45.188</map:CreatedDateTime>'
	print '<map:ModifiedBy>Administrator</map:ModifiedBy>'
	print '<map:ModifiedDateTime>2014-05-15 15:21:32.336</map:ModifiedDateTime>'
	print '</map:Overview>'
def Write_SQLExtract():
	print '<map:SourceExtractSql><map:SQLQuery xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:SQLQueryDesc xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:SourceExtractSql>'
def Write_TargetUpdateSrategy():
	print '<map:TargetUpdateStrategy><map:UpdateStrategy xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/><map:UpdateStrategyDesc xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:TargetUpdateStrategy>'
def Write_TestingNotes():
	print '<map:TestingNotes><map:TestingNotesStatus xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:TestingNotesDesc xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:TestingNotes>'
def Write_Assignments():
	print '<map:Documents/>'
	print '<map:Assignments><map:MappingDesigner/><map:MappingApprover/>'
	print '<map:MappingETLDeveloper/><map:MappingTester/></map:Assignments>'
def Write_LOE():
	print '<map:LevelOfEffort>'
	print '<map:PlannedLevelOfEffort>'
	print '<map:MappingEffort>0.0</map:MappingEffort><map:ETLEffort>0.0</map:ETLEffort><map:Notes xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:PlannedLevelOfEffort>'
	print '<map:ActualLevelOfEffort>'
	print '<map:MappingEffort>0.0</map:MappingEffort>'
	print '<map:ETLEffort>0.0</map:ETLEffort>'
	print '<map:Notes xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:ActualLevelOfEffort>'
	print '</map:LevelOfEffort>'
def Write_EndMappingDetails(project_name):
	print '<map:ChangeLog/><map:Miscellaneous>'
	print '<map:ProjectName>'+project_name+'</map:ProjectName>'
	print '<map:SubjectName/><map:SubjectHierarchy/></map:Miscellaneous>'
	print '</map:MappingDetails>'
def Write_StartMappingGrid():
	print '<map:MappingGrid>'
def Write_EndMappingGrid():
	print '</map:MappingGrid>'
def Write_EndMapping():
	print '</map:Mapping>'
def Write_Row_Start():
	print '<map:MappingRow>'
def Write_Row_End():
	print '</map:MappingRow>'
def Write_Row_Misc(rownum):
	print '<map:Miscellaneous><map:CreatedBy>Administrator</map:CreatedBy><map:CreatedDateTime>2014-05-15 11:10:45.656</map:CreatedDateTime>'
	print '<map:LastModifiedBy>Administrator</map:LastModifiedBy><map:LastModifiedDateTime>2014-05-15 15:21:32.336</map:LastModifiedDateTime>'
	print '<map:Status>N</map:Status><map:SequenceID>1</map:SequenceID>'
	print '<map:MapSpecRowComments xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:RowOrder>'+rownum+'</map:RowOrder>'
	print '<map:UserDefined1 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined2 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined3 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined4 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined5 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined6 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined7 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined8 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined9 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:UserDefined10 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:Miscellaneous>'
def Write_Row_Src(system,environment,table_name,column_name,src_data_type,src_length,src_precision,src_nullable,natural_key,identity_key,business_key):
	print '<map:SourceDetails>'
	print '<map:SystemName>'+system+'</map:SystemName>'
	print '<map:EnvironmentName>'+environment+'</map:EnvironmentName>'
	if table_name == '':
		print '<map:TableName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	else:
		print '<map:TableName>'+table_name+'</map:TableName>'
	print '<map:TableClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	if column_name == '':
		print '<map:ColumnName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	else:
		print '<map:ColumnName>'+column_name+'</map:ColumnName>'
	print '<map:DataType>'+src_data_type+'</map:DataType>'
	print '<map:Length>'+src_length+'</map:Length>'
	print '<map:Precision>'+src_precision+'</map:Precision>'
	print '<map:Scale>0</map:Scale>'
	print '<map:NullableFlag>'+src_nullable+'</map:NullableFlag>'
	print '<map:DBDefaultValue xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:Definition xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:Comments xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:NaturalKeyFlag>'+natural_key+'</map:NaturalKeyFlag>'
	print '<map:IdentityKeyFlag>'+identity_key+'</map:IdentityKeyFlag>'
	print '<map:PercentNullValue>0</map:PercentNullValue>'
	print '<map:ColumnClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:TableAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:ColumnAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:BusinessKeyFlag>'+business_key+'</map:BusinessKeyFlag>'
	print '<map:LogicalColumnName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:SDIFlag>N</map:SDIFlag>'
	print '<map:SDIDescription xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:XPath xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:MinValue>0</map:MinValue>'
	print '<map:MaxValue>0</map:MaxValue>'
	print '</map:SourceDetails>'
def Write_Row_Tgt(system,environment,table_name,column_name,tgt_data_type,tgt_length,tgt_precision,tgt_nullable,natural_key,primary_key,business_key):
	print '<map:TargetDetails>'
	print '<map:SystemName>'+system+'</map:SystemName>'
	print '<map:EnvironmentName>'+environment+'</map:EnvironmentName>'
	print '<map:TableName>'+table_name+'</map:TableName>'
	print '<map:TableClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:ColumnName>'+column_name+'</map:ColumnName>'
	print '<map:DataType>'+tgt_data_type+'</map:DataType>'
	print '<map:Length>'+tgt_length+'</map:Length>'	
	print '<map:Precision>'+tgt_precision+'</map:Precision>'
	print '<map:Scale>0</map:Scale>'
	print '<map:NullableFlag>Y</map:NullableFlag>'
	print '<map:ETLDefaultValue xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:Definition xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:Comments xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:NaturalKeyFlag>'+natural_key+'/map:NaturalKeyFlag>'
	print '<map:PrimaryKeyFlag>'+primary_key+'</map:PrimaryKeyFlag>'
	print '<map:LogicalColumn xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:ColumnClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:TableAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:ColumnAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:BusinessKeyFlag>'+business_key+'</map:BusinessKeyFlag>'
	print '<map:SDIFlag>N</map:SDIFlag>'
	print '<map:SDIDescription xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:XPath xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:TargetDetails>'
def Write_Row_Transform(business_rule):
	print '<map:TransformationDetails>'
	if business_rule == '':
		print '<map:BusinessRule xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	else:
		print '<map:BusinessRule>'+business_rule+'</map:BusinessRule>'
	print '<map:ExtendedBusinsessRule xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:TransLookupCondition xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '<map:LookupOn xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>'
	print '</map:TransformationDetails>'	
def Write_Row_Codeset():
	print '<map:CodesetDetails>'
	print '<map:MappingName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/></map:CodesetDetails>'
for doc in documents:
	filename = args.project+'_'+args.basedocname+doc+'.xml'
	print filename
	subset_df = df.loc[(df.TABLE_NAME ==doc),]
	data_file = create_file(filename)
	


Write_XSD()
Write_Overview('m_h_apln','This is for the APLN hub')
Write_SQLExtract()
Write_TargetUpdateSrategy()
Write_TestingNotes()
Write_Assignments()
Write_LOE()
Write_EndMappingDetails(args.project)
Write_StartMappingGrid()
# Begin a loop

#Write_Row_Src('DW3PRD','DW3PRD_ODSETL','ODSETL.X_REQUEST','APLN_NBR','NUMBER','22','0','N','N','N','Y')

# End loop



#print df['TARGET_TABLE']
row_count = 1.0
for count, row in df.iterrows():
	Write_Row_Start()
	src_table = row['SRC_TABLE']
	src_column = row['SRC_Column']
	src_full_data_type = row['SRC_Attribute_Data_Type']
	src_nullable = row['SRC_Nullable']
	rsrc_value = row['SRC_SYSTEM']
	tgt_table = row['TABLE_NAME']
	tgt_column = row['TGT_COLUMN_NAME']
	tgt_full_data_type = row['PHYSICAL_DATA_TYPE']
	tgt_nullable = row['TGT_Nullable']
	if type(src_table) == type(float()):
		src_table = ''
	if type(src_column) == type(float()):
		src_column = ''
	if src_full_data_type == 'SYSTEM_GENERATED' or src_full_data_type == 'INTEGER':
		src_data_type = 'NUMBER'
		src_data_type_length = '28'
		src_data_type_precision = '0'
	else:
		(src_data_type,src_data_type_length) = src_full_data_type.split('(')
		if src_data_type_length.find(',') >0:
			(src_data_type_length,src_data_type_precision) = src_data_type_length.split(',')
		else:
			src_data_type_length = src_data_type_length.strip(')')
			src_data_type_precision = '0'
	Write_Row_Src('DW3PRD','DW3PRD_ODSETL',src_table,src_column,src_data_type,src_data_type_length,src_data_type_precision,src_nullable,'N','N','Y')
	if tgt_full_data_type == 'SYSTEM_GENERATED' or tgt_full_data_type == 'INTEGER':
		tgt_data_type = 'NUMBER'
		tgt_data_type_length = '28'
		tgt_data_type_precision = '0'
	else:
		(tgt_data_type,tgt_data_type_length) = tgt_full_data_type.split('(')
		if tgt_data_type_length.find(',') >0:
			(tgt_data_type_length,tgt_data_type_precision) = tgt_data_type_length.split(',')
		else:
			tgt_data_type_length = tgt_data_type_length.strip(')')
			tgt_data_type_precision = '0'	
	Write_Row_Tgt('DW1DEV','DW1DEV_DV',tgt_table,tgt_column,tgt_data_type,tgt_data_type_length,tgt_data_type_precision,'N','N','N','Y')
	if tgt_column == 'RSRC':
		rsrc_value = '"'+rsrc_value+'"'
		Write_Row_Transform(rsrc_value)
	elif tgt_column.find('SQN') > 0:
		Write_Row_Transform('Sequence')
	elif tgt_column == 'LDTS':
		Write_Row_Transform('SYSTIMESTAMP')
	Write_Row_Codeset()
	Write_Row_Misc(str(row_count))
	Write_Row_End()	
	row_count = row_count + 1
Write_EndMappingGrid()
Write_EndMapping()