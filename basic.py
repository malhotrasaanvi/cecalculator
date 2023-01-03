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

    ######################################################
                # CONSTRUCTOR #
    ######################################################
    def __init__(self,name,revenue, TotalSocialInvestment,
    TotalEnergyGenerated, TotalNonFossilFuelEnergyGenerated,
    DirectGHGEmissions, IndirectGHGEmissions, EmissionsNeutralizedbyCarbonOffsetProjects, EmissionsOfODS, EmissionsOfNOX, EmissionsOfSOX,
    WaterWithdrawal, FreshWaterDischarge, OtherWaterDischarge, WaterRecycled,
    WasteGeneratedHazardous, WasteGeneratedNonHazardous, DivertedWaste,
    EnvironmentalFines, FlaredHydrocarbon, VentedHydrocarbon):
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

        # Add new company to database
        new_company = EnergyUtil(name,revenue, TotalSocialInvestment, 
        TotalEnergyGenerated, TotalNonFossilFuelEnergyGenerated,
        DirectGHGEmissions, IndirectGHGEmissions, EmissionsNeutralizedbyCarbonOffsetProjects, EmissionsOfODS, EmissionsOfNOX, EmissionsOfSOX,
        WaterWithdrawal, FreshWaterDischarge, OtherWaterDischarge, WaterRecycled,
        WasteGeneratedHazardous, WasteGeneratedNonHazardous, DivertedWaste,
        EnvironmentalFines, FlaredHydrocarbon, VentedHydrocarbon)
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for('list_comp'))

    return render_template('add.html',form=form)


@app.route('/list')
def list_comp():
    # Grab a list of companies from database.
    companies = EnergyUtil.query.all()
    return render_template('list.html', companies=companies)


if __name__ == '__main__':
    app.run(debug=True)
