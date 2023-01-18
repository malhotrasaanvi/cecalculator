import os
from forms import  AddForm 
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class EnergyUtil(db.Model):

    __tablename__ = 'energy'
    id = db.Column(db.Integer,primary_key = True)
    
    ####### Organization ###########
    name = db.Column(db.Text)
    revenue = db.Column(db.Float)
    TotalSocialInvestment = db.Column(db.Float)

    ######## Energy ################
    TotalEnergyGenerated = db.Column(db.Float)
    TotalNonFossilFuelEnergyGenerated = db.Column(db.Float)

    ####### GHG Emissions #########
    DirectGHGEmissions = db.Column(db.Float)
    IndirectGHGEmissions = db.Column(db.Float)
    EmissionsNeutralizedbyCarbonOffsetProjects = db.Column(db.Float)
    EmissionsOfODS = db.Column(db.Float)
    EmissionsOfNOX = db.Column(db.Float)
    EmissionsOfSOX = db.Column(db.Float)

    ####### Water #################
    WaterWithdrawal = db.Column(db.Float)
    FreshWaterDischarge = db.Column(db.Float)
    OtherWaterDischarge = db.Column(db.Float)
    WaterRecycled = db.Column(db.Float)

    ####### Waste ##################
    WasteGeneratedHazardous = db.Column(db.Float)
    WasteGeneratedNonHazardous = db.Column(db.Float)
    DivertedWaste = db.Column(db.Float)

    ####### Spillage and Fines #####
    EnvironmentalFines = db.Column(db.Float)
    FlaredHydrocarbon = db.Column(db.Float)
    VentedHydrocarbon = db.Column(db.Float)

    ######## Calculations ######### 
    calc1 = db.Column(db.Float)
    calc2 = db.Column(db.Float)
    calc3 = db.Column(db.Float)
    calc4 = db.Column(db.Float)
    calc5 = db.Column(db.Float)

    calc6 = db.Column(db.Float)
    calc7 = db.Column(db.Float)
    calc8 = db.Column(db.Float)
    calc9 = db.Column(db.Float)
    calc10 = db.Column(db.Float)

    calc11 = db.Column(db.Float)
    calc12 = db.Column(db.Float)
    calc13 = db.Column(db.Float)
    calc14 = db.Column(db.Float)
    calc15 = db.Column(db.Float)

    calc16 = db.Column(db.Float)
    calc17 = db.Column(db.Float)
    calc18 = db.Column(db.Float)
    calc19 = db.Column(db.Float)
    calc20 = db.Column(db.Float)

    calc21 = db.Column(db.Float)
    calc22 = db.Column(db.Float)
    calc23 = db.Column(db.Float)
    calc24 = db.Column(db.Float)
    calc25 = db.Column(db.Float)

    calc26 = db.Column(db.Float)



    ######################################################
                # CONSTRUCTOR #
    ######################################################
    def __init__(self,name,revenue, TotalSocialInvestment,
    TotalEnergyGenerated, TotalNonFossilFuelEnergyGenerated,
    DirectGHGEmissions, IndirectGHGEmissions, EmissionsNeutralizedbyCarbonOffsetProjects, EmissionsOfODS, EmissionsOfNOX, EmissionsOfSOX,
    WaterWithdrawal, FreshWaterDischarge, OtherWaterDischarge, WaterRecycled,
    WasteGeneratedHazardous, WasteGeneratedNonHazardous, DivertedWaste,
    EnvironmentalFines, FlaredHydrocarbon, VentedHydrocarbon,
    calc1, calc2,  calc3, calc4, calc5,
    calc6, calc7, calc8, calc9, calc10,
    calc11, calc12, calc13, calc14, calc15,
    calc16, calc17, calc18, calc19, calc20,
    calc21, calc22, calc23, calc24, calc25, 
    calc26):
        self.name = name
        self.revenue = revenue
        self.TotalSocialInvestment = TotalSocialInvestment

        self.TotalEnergyGenerated = TotalEnergyGenerated
        self.TotalNonFossilFuelEnergyGenerated = TotalNonFossilFuelEnergyGenerated

        self.DirectGHGEmissions = DirectGHGEmissions
        self.IndirectGHGEmissions = IndirectGHGEmissions
        self.EmissionsNeutralizedbyCarbonOffsetProjects = EmissionsNeutralizedbyCarbonOffsetProjects
        self.EmissionsOfODS = EmissionsOfODS
        self.EmissionsOfNOX = EmissionsOfNOX
        self.EmissionsOfSOX = EmissionsOfSOX

        self.WaterWithdrawal = WaterWithdrawal
        self.FreshWaterDischarge = FreshWaterDischarge
        self.OtherWaterDischarge = OtherWaterDischarge
        self.WaterRecycled = WaterRecycled

        self.WasteGeneratedHazardous = WasteGeneratedHazardous
        self.WasteGeneratedNonHazardous = WasteGeneratedNonHazardous
        self.DivertedWaste = DivertedWaste

        self.EnvironmentalFines = EnvironmentalFines
        self.FlaredHydrocarbon = FlaredHydrocarbon
        self.VentedHydrocarbon = VentedHydrocarbon

        self.calc1 = calc1
        self.calc2 = calc2
        self.calc3 = calc3
        self.calc4 = calc4
        self.calc5 = calc5

        self.calc6 = calc6
        self.calc7 = calc7
        self.calc8 = calc8
        self.calc9 = calc9
        self.calc10 = calc10

        self.calc11 = calc11
        self.calc12 = calc12
        self.calc13 = calc13
        self.calc14 = calc14
        self.calc15 = calc15

        self.calc16 = calc16
        self.calc17 = calc17
        self.calc18 = calc18
        self.calc19 = calc19 
        self.calc20 = calc20

        self.calc21 = calc21
        self.calc22 = calc22
        self.calc23 = calc23
        self.calc24 = calc24
        self.calc25 = calc25
        
        self.calc26 = calc26



        

    def __repr__(self):
         return f"This company has been added to the database: {self.name}"


############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_comp():
    form = AddForm()
    total = 0
    otherVar = 12
    calc1 = 0
    calc2 = 0
    calc3 = 0
    calc4 = 0
    calc5 = 0

    calc6 = 0
    calc7 = 0
    calc8 = 0
    calc9 = 0
    calc10 = 0

    calc11 = 0
    calc12 = 0
    calc13 = 0
    calc14 = 0
    calc15 = 0

    calc16 = 0
    calc17 = 0
    calc18 = 0
    calc19 = 0
    calc20 = 0

    calc21 = 0
    calc22 = 0
    calc23 = 0
    calc24 = 0
    calc25 = 0

    calc26 = 0

    mult = float(0.1)


    if form.validate_on_submit():

        ###### Organizations #######
        name = form.name.data
        revenue = form.revenue.data

        ###### Energy ########
        TotalSocialInvestment = form.TotalSocialInvestment.data
        TotalEnergyGenerated = form.TotalEnergyGenerated.data
        TotalNonFossilFuelEnergyGenerated = form.TotalNonFossilFuelEnergyGenerated.data

        ###### GHG Emissions ######
        DirectGHGEmissions = form.DirectGHGEmissions.data
        IndirectGHGEmissions = form.IndirectGHGEmissions.data
        EmissionsNeutralizedbyCarbonOffsetProjects = form.EmissionsNeutralizedbyCarbonOffsetProjects.data
        EmissionsOfODS = form.EmissionsOfODS.data
        EmissionsOfNOX = form.EmissionsOfNOX.data
        EmissionsOfSOX = form.EmissionsOfSOX.data

        ###### Water #############
        WaterWithdrawal = form.WaterWithdrawal.data
        FreshWaterDischarge = form.FreshWaterDischarge.data
        OtherWaterDischarge = form.OtherWaterDischarge.data
        WaterRecycled = form.WaterRecycled.data

        ###### Waste ############
        WasteGeneratedHazardous = form.WasteGeneratedHazardous.data
        WasteGeneratedNonHazardous = form.WasteGeneratedNonHazardous.data
        DivertedWaste = form.DivertedWaste.data

        #### Spillage and Fines ###
        EnvironmentalFines = form.EnvironmentalFines.data
        FlaredHydrocarbon = form.FlaredHydrocarbon.data
        VentedHydrocarbon = form.VentedHydrocarbon.data

        total = revenue
        otherVar = revenue + TotalSocialInvestment
        calc1 = TotalEnergyGenerated - TotalNonFossilFuelEnergyGenerated
        calc2 =  calc2 = TotalNonFossilFuelEnergyGenerated / TotalEnergyGenerated
        calc3 = (DirectGHGEmissions + IndirectGHGEmissions - TotalNonFossilFuelEnergyGenerated) * 1000 / TotalEnergyGenerated
        calc4 = EmissionsOfODS / TotalEnergyGenerated
        calc5 =  EmissionsOfNOX/EmissionsOfSOX * 1000 / TotalEnergyGenerated

        calc6 = WaterRecycled / WaterWithdrawal
        calc7 = WaterWithdrawal - (FreshWaterDischarge + OtherWaterDischarge)
        calc8 = OtherWaterDischarge / (FreshWaterDischarge + OtherWaterDischarge)
        calc9 = (WaterWithdrawal - (FreshWaterDischarge + OtherWaterDischarge)) / WaterWithdrawal
        calc10 = WasteGeneratedHazardous + WasteGeneratedNonHazardous

        calc11 = (WasteGeneratedHazardous + WasteGeneratedNonHazardous) - DivertedWaste
        calc12 = WasteGeneratedHazardous / (WasteGeneratedHazardous + WasteGeneratedNonHazardous)
        calc13 = DivertedWaste / (WasteGeneratedHazardous + WasteGeneratedNonHazardous)
        calc14 = EnvironmentalFines * 100 / TotalEnergyGenerated
        calc15 = FlaredHydrocarbon / TotalEnergyGenerated

        calc16 = VentedHydrocarbon / TotalEnergyGenerated
        calc17 = 1 - (WasteGeneratedHazardous + WasteGeneratedNonHazardous) - DivertedWaste
        calc18 = DivertedWaste / (WasteGeneratedHazardous + WasteGeneratedNonHazardous)
        calc19 = WaterRecycled / WaterWithdrawal
        calc20 = 1 - OtherWaterDischarge / (FreshWaterDischarge + OtherWaterDischarge)

        calc21 = 1 - (WaterWithdrawal - (FreshWaterDischarge + OtherWaterDischarge)) / WaterWithdrawal
        calc22 = TotalNonFossilFuelEnergyGenerated / TotalEnergyGenerated
        calc23 = 1 - (DirectGHGEmissions + IndirectGHGEmissions - TotalNonFossilFuelEnergyGenerated) * 1000 / TotalEnergyGenerated / EnvironmentalFines*100 / TotalEnergyGenerated
        ### calc 24 needs to be divided by 0.1 but having trouble with that so i multiplied by 10
        calc24 = 1 - EmissionsOfODS / TotalEnergyGenerated * 10
        calc25 = 1 - EmissionsOfNOX/EmissionsOfSOX * 1000 / TotalEnergyGenerated
        calc26 = 1 - EnvironmentalFines * 100 / TotalEnergyGenerated
    
    
    
        

        # Add new company to database
        new_company = EnergyUtil(name,revenue, TotalSocialInvestment, 
        TotalEnergyGenerated, TotalNonFossilFuelEnergyGenerated,
        DirectGHGEmissions, IndirectGHGEmissions, EmissionsNeutralizedbyCarbonOffsetProjects, EmissionsOfODS, EmissionsOfNOX, EmissionsOfSOX,
        WaterWithdrawal, FreshWaterDischarge, OtherWaterDischarge, WaterRecycled,
        WasteGeneratedHazardous, WasteGeneratedNonHazardous, DivertedWaste,
        EnvironmentalFines, FlaredHydrocarbon, VentedHydrocarbon, calc1, calc2, calc3, calc4, calc5,
        calc6, calc7, calc8, calc9, calc10,
        calc11, calc12, calc13, calc14, calc15,
        calc16, calc17, calc18, calc19, calc20, 
        calc21, calc22, calc23, calc24, calc25, 
        calc26)
        db.session.add(new_company)
        db.session.commit()

        

        

        ##return redirect(url_for('list_comp'))

    return render_template('add.html',form=form, total=total, otherVar=otherVar, calc1=calc1, calc2=calc2, calc3=calc3, calc4=calc4, calc5=calc5,
    calc6=calc6, calc7=calc7, calc8=calc8, calc9=calc9, calc10=calc10, calc11=calc11, calc12=calc12, calc13=calc13, 
    calc14=calc14, calc15=calc15, calc16=calc16, calc17=calc17, calc18=calc18, calc19=calc19, calc20=calc20,
    calc21=calc21, calc22=calc22, calc23=calc23, calc24=calc24, calc25=calc25, calc26=calc26)



@app.route('/list')
def list_comp():
    # Grab a list of companies from database.
    companies = EnergyUtil.query.all()
    return render_template('list.html', companies=companies)


if __name__ == '__main__':
    app.run(debug=True)