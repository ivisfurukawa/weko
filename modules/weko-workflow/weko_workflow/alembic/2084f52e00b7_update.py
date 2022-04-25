#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""update"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2084f52e00b7'
down_revision = 'd130b9cff95c'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(op.f('fk_workflow_workflow_location_id_files_location'), 'workflow_workflow', 'files_location', ['location_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_workflow_workflow_location_id_files_location'), 'workflow_workflow', type_='foreignkey')
    # ### end Alembic commands ###