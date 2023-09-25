import Head from 'next/head'
import Image from 'next/image'
import NormalLayout from 'components/layouts/NormalLayout'
import ViewProductDetail from 'components/Products/ViewProductDetail'

export default function ViewProductDetailPage() {
    return (
        <ViewProductDetail />
    )
}


ViewProductDetailPage.getLayout = function getLayout(page) {
    return (
        <NormalLayout>
            {page}
        </NormalLayout>
    )
}