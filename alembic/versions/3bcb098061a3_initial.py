"""initial

Revision ID: 3bcb098061a3
Revises: 
Create Date: 2023-04-30 15:54:09.924541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bcb098061a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=True)
    op.create_table('important',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('level', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('level')
    )
    op.create_index(op.f('ix_important_id'), 'important', ['id'], unique=True)
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('important_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['important_id'], ['important.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_category_id'), 'task', ['category_id'], unique=False)
    op.create_index(op.f('ix_task_id'), 'task', ['id'], unique=True)
    op.create_index(op.f('ix_task_important_id'), 'task', ['important_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_important_id'), table_name='task')
    op.drop_index(op.f('ix_task_id'), table_name='task')
    op.drop_index(op.f('ix_task_category_id'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_important_id'), table_name='important')
    op.drop_table('important')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###