// 
// *  This file was automatically generated by MoMEMta-MaGMEE,
// *  A MadGraph Matrix Element Exporter plugin for MoMEMta.
// *
// *  It is subject to MoMEMta-MaGMEE's license and copyright:
// *
// *  Copyright (C) 2016  Universite catholique de Louvain (UCL), Belgium
// *
// *  This program is free software: you can redistribute it and/or modify
// *  it under the terms of the GNU General Public License as published by
// *  the Free Software Foundation, either version 3 of the License, or
// *  (at your option) any later version.
// *
// *  This program is distributed in the hope that it will be useful,
// *  but WITHOUT ANY WARRANTY; without even the implied warranty of
// *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// *  GNU General Public License for more details.
// *
// *  You should have received a copy of the GNU General Public License
// *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
// 

#pragma once

#include <complex> 
#include <vector> 
#include <utility> 
#include <map> 
#include <functional> 

#include <Parameters_sm.h> 
#include <SubProcess.h> 

#include <momemta/MatrixElement.h> 

namespace dy_to_ll_sm 
{

//==========================================================================
// A class for calculating the matrix elements for
// Process: g g > z b b~ WEIGHTED<=4 @1
// *   Decay: z > e+ e- WEIGHTED<=2
//--------------------------------------------------------------------------

class P1_Sigma_sm_gg_epembbx: public momemta::MatrixElement 
{
  public:

    // Constructor & destructor
    P1_Sigma_sm_gg_epembbx(const ParameterSet& configuration); 
    virtual ~P1_Sigma_sm_gg_epembbx() {}; 

    // Calculate flavour-independent parts of cross section.
    virtual momemta::MatrixElement::Result compute(
    const std::pair < std::vector<double> , std::vector<double> >
        &initialMomenta,
    const std::vector < std::pair < int, std::vector<double> > > &finalState); 

    virtual std::shared_ptr < momemta::MEParameters > getParameters() 
    {
      return params; 
    }

    // Make sure all helicity combinations are tried again (forget optimisation
    // consisting of not evaluating helicities which have given a zero result
    // once)
    virtual void resetHelicities(); 

  private:

    // default constructor should be hidden
    P1_Sigma_sm_gg_epembbx() = delete; 

    // list of helicities combinations
    const int helicities[64][6] = {{-1, -1, -1, -1, -1, -1}, {-1, -1, -1, -1,
        -1, 1}, {-1, -1, -1, -1, 1, -1}, {-1, -1, -1, -1, 1, 1}, {-1, -1, -1,
        1, -1, -1}, {-1, -1, -1, 1, -1, 1}, {-1, -1, -1, 1, 1, -1}, {-1, -1,
        -1, 1, 1, 1}, {-1, -1, 1, -1, -1, -1}, {-1, -1, 1, -1, -1, 1}, {-1, -1,
        1, -1, 1, -1}, {-1, -1, 1, -1, 1, 1}, {-1, -1, 1, 1, -1, -1}, {-1, -1,
        1, 1, -1, 1}, {-1, -1, 1, 1, 1, -1}, {-1, -1, 1, 1, 1, 1}, {-1, 1, -1,
        -1, -1, -1}, {-1, 1, -1, -1, -1, 1}, {-1, 1, -1, -1, 1, -1}, {-1, 1,
        -1, -1, 1, 1}, {-1, 1, -1, 1, -1, -1}, {-1, 1, -1, 1, -1, 1}, {-1, 1,
        -1, 1, 1, -1}, {-1, 1, -1, 1, 1, 1}, {-1, 1, 1, -1, -1, -1}, {-1, 1, 1,
        -1, -1, 1}, {-1, 1, 1, -1, 1, -1}, {-1, 1, 1, -1, 1, 1}, {-1, 1, 1, 1,
        -1, -1}, {-1, 1, 1, 1, -1, 1}, {-1, 1, 1, 1, 1, -1}, {-1, 1, 1, 1, 1,
        1}, {1, -1, -1, -1, -1, -1}, {1, -1, -1, -1, -1, 1}, {1, -1, -1, -1, 1,
        -1}, {1, -1, -1, -1, 1, 1}, {1, -1, -1, 1, -1, -1}, {1, -1, -1, 1, -1,
        1}, {1, -1, -1, 1, 1, -1}, {1, -1, -1, 1, 1, 1}, {1, -1, 1, -1, -1,
        -1}, {1, -1, 1, -1, -1, 1}, {1, -1, 1, -1, 1, -1}, {1, -1, 1, -1, 1,
        1}, {1, -1, 1, 1, -1, -1}, {1, -1, 1, 1, -1, 1}, {1, -1, 1, 1, 1, -1},
        {1, -1, 1, 1, 1, 1}, {1, 1, -1, -1, -1, -1}, {1, 1, -1, -1, -1, 1}, {1,
        1, -1, -1, 1, -1}, {1, 1, -1, -1, 1, 1}, {1, 1, -1, 1, -1, -1}, {1, 1,
        -1, 1, -1, 1}, {1, 1, -1, 1, 1, -1}, {1, 1, -1, 1, 1, 1}, {1, 1, 1, -1,
        -1, -1}, {1, 1, 1, -1, -1, 1}, {1, 1, 1, -1, 1, -1}, {1, 1, 1, -1, 1,
        1}, {1, 1, 1, 1, -1, -1}, {1, 1, 1, 1, -1, 1}, {1, 1, 1, 1, 1, -1}, {1,
        1, 1, 1, 1, 1}};

    // Private functions to calculate the matrix element for all subprocesses
    // Wavefunctions
    void calculate_wavefunctions(const int perm[], const int hel[]); 
    std::complex<double> amp[8]; 

    // Matrix elements
    double matrix_1_gg_zbbx_z_epem(); 

    // map of final states
    std::map < std::vector<int> , std::vector < SubProcess <
        P1_Sigma_sm_gg_epembbx >> > mapFinalStates;

    // Reference to the model parameters instance passed in the constructor
    std::shared_ptr < Parameters_sm > params; 

    // vector with external particle masses
    std::vector < std::reference_wrapper<double> > mME; 

    // vector with momenta (to be changed each event)
    double * momenta[6]; 
}; 


}

