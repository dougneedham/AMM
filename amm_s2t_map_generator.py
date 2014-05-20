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
def Write_XSD(file_handle):
	file_handle.write('<?xml version="1.0" encoding="UTF-8"?>\n')
	file_handle.write('<map:Mapping version="1.0" xmlns:map="www.analytixds.com/amm/xml/mapping">\n')
	file_handle.write('<map:MappingDetails>\n')	
	
def Write_Overview(file_handle,mapping_name,description):
	file_handle.write('<map:Overview>\n')
	file_handle.write('<map:SpecificationName>'+mapping_name + '</map:SpecificationName>\n')
	file_handle.write('<map:MapSpecVersion>1</map:MapSpecVersion>\n')
	file_handle.write('<map:VersionLabel> </map:VersionLabel>\n')
	file_handle.write('<map:JobNameXRef xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:MappingDescription>'+ description +'</map:MappingDescription>\n')
	file_handle.write('<map:CreatedBy>Administrator</map:CreatedBy>\n')
	file_handle.write('<map:CreatedDateTime>2014-05-15 11:06:45.188</map:CreatedDateTime>\n')
	file_handle.write('<map:ModifiedBy>Administrator</map:ModifiedBy>\n')
	file_handle.write('<map:ModifiedDateTime>2014-05-15 15:21:32.336</map:ModifiedDateTime>\n')
	file_handle.write('</map:Overview>\n')
def Write_SQLExtract(file_handle):
	file_handle.write('<map:SourceExtractSql><map:SQLQuery xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:SQLQueryDesc xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:SourceExtractSql>\n')
def Write_TargetUpdateSrategy(file_handle):
	file_handle.write('<map:TargetUpdateStrategy>\n')
	file_handle.write('<map:UpdateStrategy xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UpdateStrategyDesc xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:TargetUpdateStrategy>\n')
def Write_TestingNotes(file_handle):
	file_handle.write('<map:TestingNotes>\n')
	file_handle.write('<map:TestingNotesStatus xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:TestingNotesDesc xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:TestingNotes>\n')
def Write_Assignments(file_handle):
	file_handle.write('<map:Documents/>\n')
	file_handle.write('<map:Assignments><map:MappingDesigner/><map:MappingApprover/>\n')
	file_handle.write('<map:MappingETLDeveloper/><map:MappingTester/></map:Assignments>\n')
def Write_LOE(file_handle):
	file_handle.write('<map:LevelOfEffort>\n')
	file_handle.write('<map:PlannedLevelOfEffort>\n')
	file_handle.write('<map:MappingEffort>0.0</map:MappingEffort>\n')
	file_handle.write('<map:ETLEffort>0.0</map:ETLEffort>\n')
	file_handle.write('<map:Notes xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:PlannedLevelOfEffort>\n')
	file_handle.write('<map:ActualLevelOfEffort>\n')
	file_handle.write('<map:MappingEffort>0.0</map:MappingEffort>\n')
	file_handle.write('<map:ETLEffort>0.0</map:ETLEffort>\n')
	file_handle.write('<map:Notes xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:ActualLevelOfEffort>\n')
	file_handle.write('</map:LevelOfEffort>\n')
def Write_EndMappingDetails(file_handle,project_name):
	file_handle.write('<map:ChangeLog/><map:Miscellaneous>\n')
	file_handle.write('<map:ProjectName>'+project_name+'</map:ProjectName>\n')
	file_handle.write('<map:SubjectName/>\n')
	file_handle.write('<map:SubjectHierarchy/>\n')
	file_handle.write('</map:Miscellaneous>\n')
	file_handle.write('</map:MappingDetails>\n')
def Write_StartMappingGrid(file_handle):
	file_handle.write('<map:MappingGrid>\n')
def Write_EndMappingGrid(file_handle):
	file_handle.write('</map:MappingGrid>\n')
def Write_EndMapping(file_handle):
	file_handle.write('</map:Mapping>\n')
def Write_Row_Start(file_handle):
	file_handle.write('<map:MappingRow>\n')
def Write_Row_End(file_handle):
	file_handle.write('</map:MappingRow>\n')
def Write_Row_Misc(file_handle,rownum):
	file_handle.write('<map:Miscellaneous>\n')
	file_handle.write('<map:CreatedBy>Administrator</map:CreatedBy>\n')
	file_handle.write('<map:CreatedDateTime>2014-05-15 11:10:45.656</map:CreatedDateTime>\n')
	file_handle.write('<map:LastModifiedBy>Administrator</map:LastModifiedBy>\n')
	file_handle.write('<map:LastModifiedDateTime>2014-05-15 15:21:32.336</map:LastModifiedDateTime>\n')
	file_handle.write('<map:Status>N</map:Status>\n')
	file_handle.write('<map:SequenceID>'+str(int(float(rownum)))+'</map:SequenceID>\n')
	file_handle.write('<map:MapSpecRowComments xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:RowOrder>'+rownum+'</map:RowOrder>\n')
	file_handle.write('<map:UserDefined1 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined2 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined3 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined4 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined5 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined6 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined7 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined8 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined9 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:UserDefined10 xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:Miscellaneous>\n')
def Write_Row_Src(file_handle,system,environment,table_name,column_name,src_data_type,src_length,src_precision,src_nullable,natural_key,identity_key,business_key):
	file_handle.write('<map:SourceDetails>\n')
	if system == '':
		file_handle.write('<map:SystemName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	else:
		file_handle.write('<map:SystemName>'+system+'</map:SystemName>\n')
	if environment == '':
		file_handle.write('<map:EnvironmentName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	else:
		file_handle.write('<map:EnvironmentName>'+environment+'</map:EnvironmentName>\n')
	if table_name == '':
		file_handle.write('<map:TableName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	else:
		file_handle.write('<map:TableName>'+table_name+'</map:TableName>\n')
	file_handle.write('<map:TableClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	if column_name == '':
		file_handle.write('<map:ColumnName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	else:
		file_handle.write('<map:ColumnName>'+column_name+'</map:ColumnName>\n')
	if src_data_type == '':
		file_handle.write('<map:DataType xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	else:
		file_handle.write('<map:DataType>'+src_data_type+'</map:DataType>\n')
	file_handle.write('<map:Length>'+src_length+'</map:Length>\n')
	file_handle.write('<map:Precision>'+src_precision+'</map:Precision>\n')
	file_handle.write('<map:Scale>0</map:Scale>\n')
	file_handle.write('<map:NullableFlag>'+src_nullable+'</map:NullableFlag>\n')
	file_handle.write('<map:DBDefaultValue xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:Definition xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:Comments xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:NaturalKeyFlag>'+natural_key+'</map:NaturalKeyFlag>\n')
	file_handle.write('<map:IdentityKeyFlag>'+identity_key+'</map:IdentityKeyFlag>\n')
	file_handle.write('<map:PercentNullValue>0</map:PercentNullValue>\n')
	file_handle.write('<map:ColumnClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:TableAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:ColumnAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:BusinessKeyFlag>'+business_key+'</map:BusinessKeyFlag>\n')
	file_handle.write('<map:LogicalColumnName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:SDIFlag>N</map:SDIFlag>\n')
	file_handle.write('<map:SDIDescription xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:XPath xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:MinValue>0</map:MinValue>\n')
	file_handle.write('<map:MaxValue>0</map:MaxValue>\n')
	file_handle.write('</map:SourceDetails>\n')
def Write_Row_Tgt(file_handle,system,environment,table_name,column_name,tgt_data_type,tgt_length,tgt_precision,tgt_nullable,natural_key,primary_key,business_key):
	file_handle.write('<map:TargetDetails>\n')
	file_handle.write('<map:SystemName>'+system+'</map:SystemName>\n')
	file_handle.write('<map:EnvironmentName>'+environment+'</map:EnvironmentName>\n')
	file_handle.write('<map:TableName>DV.'+table_name+'</map:TableName>\n')
	file_handle.write('<map:TableClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:ColumnName>'+column_name+'</map:ColumnName>\n')
	file_handle.write('<map:DataType>'+tgt_data_type+'</map:DataType>\n')
	file_handle.write('<map:Length>'+tgt_length+'</map:Length>\n')	
	file_handle.write('<map:Precision>'+tgt_precision+'</map:Precision>\n')
	file_handle.write('<map:Scale>0</map:Scale>\n')
	file_handle.write('<map:NullableFlag>'+tgt_nullable+'</map:NullableFlag>\n')
	file_handle.write('<map:ETLDefaultValue xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:Definition xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:Comments xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:NaturalKeyFlag>'+natural_key+'</map:NaturalKeyFlag>\n')
	file_handle.write('<map:PrimaryKeyFlag>'+primary_key+'</map:PrimaryKeyFlag>\n')
	file_handle.write('<map:LogicalColumn xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:ColumnClass xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:TableAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:ColumnAlias xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:BusinessKeyFlag>'+business_key+'</map:BusinessKeyFlag>\n')
	file_handle.write('<map:SDIFlag>N</map:SDIFlag>\n')
	file_handle.write('<map:SDIDescription xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:XPath xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:TargetDetails>\n')
def Write_Row_Transform(file_handle,business_rule):
	file_handle.write('<map:TransformationDetails>\n')
	if business_rule == '':
		file_handle.write('<map:BusinessRule xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	else:
		file_handle.write('<map:BusinessRule>'+business_rule+'</map:BusinessRule>\n')
	file_handle.write('<map:ExtendedBusinsessRule xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:TransLookupCondition xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('<map:LookupOn xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:TransformationDetails>\n')	
def Write_Row_Codeset(file_handle):
	file_handle.write('<map:CodesetDetails>\n')
	file_handle.write('<map:MappingName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>\n')
	file_handle.write('</map:CodesetDetails>\n')
for doc in documents:
	filename = args.project+'_'+args.basedocname+doc+'.xml'
	print filename
	subset_df = df.loc[(df.TABLE_NAME ==doc),]
	file_handle = create_file(filename)
	Write_XSD(file_handle)
	Write_Overview(file_handle,args.basedocname+doc,'This is for a hub')
	Write_SQLExtract(file_handle)
	Write_TargetUpdateSrategy(file_handle)
	Write_TestingNotes(file_handle)
	Write_Assignments(file_handle)
	Write_LOE(file_handle)
	Write_EndMappingDetails(file_handle,args.project)
	Write_StartMappingGrid(file_handle)
	# Begin a loop

	#Write_Row_Src('DW3PRD','DW3PRD_ODSETL','ODSETL.X_REQUEST','APLN_NBR','NUMBER','22','0','N','N','N','Y')

	# End loop



	#print df['TARGET_TABLE']
	row_count = 1.0
	for count, row in subset_df.iterrows():
		Write_Row_Start(file_handle)
		src_table = row['SRC_TABLE']
		src_column = row['SRC_Column']
		src_full_data_type = row['SRC_Attribute_Data_Type']
		src_nullable = row['SRC_Nullable']
		rsrc_value = row['SRC_SYSTEM']
		tgt_table = row['TABLE_NAME']
		tgt_column = row['TGT_COLUMN_NAME']
		tgt_full_data_type = row['PHYSICAL_DATA_TYPE']
		tgt_nullable = row['TGT_Nullable']
		tgt_primary_key = row['TGT_PK']
		src_business_key = 'N'		
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
				src_data_type_precision = src_data_type_precision.strip(')')				
			else:
				src_data_type_length = src_data_type_length.strip(')')
				src_data_type_precision = '0'
		if src_table == '':
			src_system = ''
			src_environment = ''
			src_data_type = ''
			src_data_type_length = '0'
			src_data_type_precesion = '0'
			src_business_key = 'N'
		else:
			src_system = 'DW3PRD'
			src_environment = 'DW3PRD_ODSETL'
		
		Write_Row_Src(file_handle,src_system,src_environment,src_table,src_column,src_data_type,src_data_type_length,src_data_type_precision,src_nullable,'N','N',src_business_key)
		if tgt_full_data_type == 'SYSTEM_GENERATED' or tgt_full_data_type == 'INTEGER':
			tgt_data_type = 'NUMBER'
			tgt_data_type_length = '28'
			tgt_data_type_precision = '0'
		else:
			(tgt_data_type,tgt_data_type_length) = tgt_full_data_type.split('(')
			if tgt_data_type_length.find(',') >0:
				(tgt_data_type_length,tgt_data_type_precision) = tgt_data_type_length.split(',')
				tgt_data_type_precision = tgt_data_type_precision.strip(')')
			else:
				tgt_data_type_length = tgt_data_type_length.strip(')')
				tgt_data_type_precision = '0'	
		Write_Row_Tgt(file_handle,'DW1DEV','DW1DEV_DV',tgt_table,tgt_column,tgt_data_type,tgt_data_type_length,tgt_data_type_precision,tgt_nullable,'N',tgt_primary_key,src_business_key)
		if tgt_column == 'RSRC':
			rsrc_value = '"'+rsrc_value+'"'
			Write_Row_Transform(file_handle,rsrc_value)
		elif tgt_column.find('SQN') > 0:
			Write_Row_Transform(file_handle,'Sequence')
		elif tgt_column == 'LDTS':
			Write_Row_Transform(file_handle,'SYSTIMESTAMP')
		else: 
			Write_Row_Transform(file_handle,'')
		Write_Row_Codeset(file_handle)
		Write_Row_Misc(file_handle,str(row_count))
		Write_Row_End(file_handle)	
		row_count = row_count + 1
	Write_EndMappingGrid(file_handle)
	Write_EndMapping(file_handle)
	file_handle.close()