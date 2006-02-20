# -*- coding: utf-8 -*-
## CMFPlacefulWorkflow
## A CMF/Plone product for locally changing the workflow of content types
## Copyright (C)2006 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
Initialization
"""
__version__ = "$Revision$"
# $Source: /cvsroot/ingeniweb/CMFPlacefulWorkflow/__init__.py,v $
# $Id$
__docformat__ = 'restructuredtext'

# Apply monkey patches
import patches

import PlacefulWorkflowTool
import DefaultWorkflowPolicy
import WorkflowPolicyConfig

from Products.CMFCore import utils, DirectoryView

from global_symbols import *

from AccessControl.Permissions import *

install_globals = globals()          # Used only in the Extensions/Install.py script

from Products.CMFCore.utils import registerIcon

from Products.CMFCore import utils

tools = (PlacefulWorkflowTool.PlacefulWorkflowTool, )

DirectoryView.registerDirectory('skins', globals())

# Initialization method
def initialize(context):


    registerIcon( DefaultWorkflowPolicy.DefaultWorkflowPolicyDefinition
                , 'images/workflow_policy.gif'
                , globals()
                )

    context.registerClass(
        PlacefulWorkflowTool.PlacefulWorkflowTool,
        meta_type="Placeful Workflow Tool",
        constructors=(PlacefulWorkflowTool.addPlacefulWorkflowTool,),
        icon = 'tool.gif')

    context.registerClass(
        WorkflowPolicyConfig.WorkflowPolicyConfig,
        permission='Add Workflow Policy',
        constructors=(WorkflowPolicyConfig.manage_addWorkflowPolicyConfigForm,
                      WorkflowPolicyConfig.manage_addWorkflowPolicyConfig),
        icon='www/WorkflowPolicyConfig_icon.gif',
    )

    utils.ToolInit( 'CMF Placeful Workflow Tool'
                  , tools=tools
                  , product_name='CMFPlacefulWorkflow'
                  , icon='tool.gif'
                  ).initialize( context )
