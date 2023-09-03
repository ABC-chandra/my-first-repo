import psycopg2
import xlsxwriter

hostname ="54.242.197.47"
database ="IMEIDBNSX"
username ="imeidbreports"
pwd="Imeidb_Report$1201$"
port_id =5444


conn =psycopg2.connect(
        dbname=database,
        host=hostname,
        user=username,
        password=pwd,
        port=port_id)
cur = conn.cursor()


cur.execute("select 'Venus_GEO_NSX','EXISTING CUSTOMER/MEMBER','','','','','Managed Services','CLOSED','',du.first_name,du.sur_name,du.job_title,od.org_name,du.email,'','','','','','',od.country,'','','','GSMA SERVICES','Services - OEM','OEM'
from imeidb.dsd_organisation od, imeidb.dsd_organisation_users du where od.org_id=du.org_id and od.org_type='OEM' AND DU.IS_ACTIVE='Y' order by 6 ")
row=1
col=0
workbook = xlsxwriter.Workbook('Downloads\\Weekly_OEM_Contact_Details_Report.xlsx')
worksheet = workbook.add_worksheet('OEMs_Details')
for i in cur.fetchall():
    worksheet.write(row, col,  i[0])
    worksheet.write(row, col+1,  i[1])
    worksheet.write(row, col+2,  i[2])
    worksheet.write(row, col+3,  i[3])
    row += 1


worksheet.write(0, 0,  'Lead Source Description')
worksheet.write(0, 1,  'Lead Source Most Recent')
worksheet.write(0, 2,  'Lead Source Description')
worksheet.write(0, 3,  'Record Type ID')
worksheet.write(0, 4,  'Owner ID')
worksheet.write(0, 5,  'Campaign ID')
worksheet.write(0, 6,  'Lead Owner')
worksheet.write(0, 7, 'Lead Stage')
worksheet.write(0, 8, 'Salutation')
worksheet.write(0, 9, 'First Name')
worksheet.write(0, 10, 'Job Title')
worksheet.write(0, 11, 'Company')
worksheet.write(0, 12, 'Email')
worksheet.write(0, 13, 'Mobile')
worksheet.write(0, 14, 'Phone')
worksheet.write(0, 15, 'Street')
worksheet.write(0, 16, 'City')
worksheet.write(0, 17,  'State')
worksheet.write(0, 18, 'Zip')
worksheet.write(0, 19, 'Country')
worksheet.write(0, 20, 'Website')
worksheet.write(0, 21, 'Product Interest')
worksheet.write(0, 22, 'Specific Interest')
worksheet.write(0, 23, 'Marketing Interest')
worksheet.write(0, 24, 'Marketing Sub-Interest')
worksheet.write(0, 25, 'Type of Account')
worksheet.write(0, 26, 'GDPR Email Consent?')
worksheet.write(0, 27, 'Consent Date')
worksheet.write(0, 28, 'Consent Source')
worksheet.write(0, 29, 'Consent Text')
workbook.close()
