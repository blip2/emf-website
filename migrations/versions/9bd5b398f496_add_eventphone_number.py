"""Add eventphone_number

Revision ID: 9bd5b398f496
Revises: 70fd4360eb2b
Create Date: 2022-05-17 01:17:05.706684

"""

# revision identifiers, used by Alembic.
revision = '9bd5b398f496'
down_revision = '70fd4360eb2b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposal', sa.Column('eventphone_number', sa.String(), nullable=True))
    op.add_column('proposal_version', sa.Column('eventphone_number', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposal_version', 'eventphone_number')
    op.drop_column('proposal', 'eventphone_number')
    # ### end Alembic commands ###
