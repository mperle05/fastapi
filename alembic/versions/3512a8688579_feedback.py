"""feedback

Revision ID: 3512a8688579
Revises: 0a0ce2967aee
Create Date: 2023-06-02 21:29:18.370402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3512a8688579'
down_revision = '0a0ce2967aee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('feedback',sa.Column('id', 
                    sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    op.add_column('feedback', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_table('feedback')
    pass
