"""add columns to exercises

Revision ID: 7442056b9f37
Revises: 6c0606f36c69
Create Date: 2025-08-27 00:54:52.736074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7442056b9f37'
down_revision: Union[str, None] = '6c0606f36c69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

def upgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    columns = [col['name'] for col in inspector.get_columns('exercises')]
    
    if 'muscle_group' not in columns:
        op.add_column('exercises', sa.Column('muscle_group', sa.String(), nullable=True))
    if 'equipment' not in columns:
        op.add_column('exercises', sa.Column('equipment', sa.String(), nullable=True))
    if 'description' not in columns:
        op.add_column('exercises', sa.Column('description', sa.String(), nullable=True))



def downgrade() -> None:
    op.drop_column('exercises', 'description')
    op.drop_column('exercises', 'equipment')
    op.drop_column('exercises', 'muscle_group')
