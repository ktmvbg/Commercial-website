import Head from 'next/head'
import Image from 'next/image'
import NormalLayout from 'components/layouts/NormalLayout'
import ViewProducts from 'components/Products/ViewProducts'

export default function ViewProductsPage() {
    return (
        <ViewProducts />
    )
}


ViewProductsPage.getLayout = function getLayout(page) {
    return (
        <NormalLayout>
            {page}
        </NormalLayout>
    )
}