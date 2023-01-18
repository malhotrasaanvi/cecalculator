from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField



class AddForm(FlaskForm):

    name = StringField('Name of company:')
    revenue = DecimalField('What is your annual revenue? (in millions of dollars): ')
    TotalSocialInvestment = DecimalField('Do you socially invest for environmental sustainability? If so, how much?')

    ######### Energy ###########
    TotalEnergyGenerated = DecimalField('What is the total amount of energy you have generated this year? (Please keep units consistent and please report in Joules or Multiples)')
    TotalNonFossilFuelEnergyGenerated = DecimalField('What is the total amount of Non Fossil Fuel energy you have generated this year? (Please keep units consistent and please report in Joules or Multiples)')

    ###### GHG Emissions #######
    DirectGHGEmissions = DecimalField('Please provide the total direct GHG emissions  in tonnes (Also known as Scope 1 Emissions)')
    IndirectGHGEmissions = DecimalField('Please provide the total indirect GHG emissions  in tonnes (Also known as Scope 2 Emissions)')
    EmissionsNeutralizedbyCarbonOffsetProjects = DecimalField('Please provide is the total annual offset of CO2 equivalent emission in tonnes, if any')
    EmissionsOfODS = DecimalField('Please provide the total metric tonnes of ODS emissions')
    EmissionsOfNOX = DecimalField('Please provide the total NOX emissions in kg or multiples')
    EmissionsOfSOX = DecimalField('Please provide the total SOX emissions in kg or multiples')

    ####### Water #########
    WaterWithdrawal = DecimalField('Please report the total volume of water consumption this year ')
    FreshWaterDischarge = DecimalField('Please report the annual total freshwater discharge ')
    OtherWaterDischarge = DecimalField('Please report the annual total OTHER (non-freshwater) discharge ')
    WaterRecycled = DecimalField('Please report the total annual volume of water recycled or reused ')

    ###### Waste #########
    WasteGeneratedHazardous = DecimalField('Please report the annual total amount of hazardous waste generated (weight)')
    WasteGeneratedNonHazardous = DecimalField('Please report the annual total amount of non-hazardous waste generated (weight)')
    DivertedWaste = DecimalField('Please report the annual total amount of diverted waste from disposal (reused, recycled, recovered) (weight)')

    ##### Spillage and Fines ###
    EnvironmentalFines = DecimalField('Please report the annual total amount of environmental fines you had to pay ')
    FlaredHydrocarbon = DecimalField('Please report the volume of flared hydrocarbons, if any.')
    VentedHydrocarbon = DecimalField('Please report the volume of vented hydrocarbons, if any.')
    submit = SubmitField('Calculate your circularity')
